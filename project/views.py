from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from django.template import RequestContext
from project.models import Project_title
from django.db.models import Q
class MapForm(forms.Form):
    map = forms.Field(
                        widget=GoogleMap(
                            attrs={
                            'width':910, 'height':510
                            }
                            )
                        )
def pin_position(xyam,yyam,gmap):

	marker = maps.Marker(opts = {
	    'map': gmap,
        'position': maps.LatLng(xyam, yyam),
    					})
     	return marker

def index(request):
    "intialize gmap with initial center location"
    gmap = maps.Map(opts = {
        'center': maps.LatLng(18, 72.5),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 1,
        'mapTypeControlOptions': {
            'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    """ This is project location  """

    position_list = Project_title.objects.all().values_list('lat','lng','project_title','Country','Status','Type_of_units','Starting_Price','Ending_Price')
    for each_position in position_list:
        marker = pin_position(each_position[0],each_position[1],gmap)
        each_position_id = Project_title.objects.get(Q(lat__exact=each_position[0]),Q(lng__exact=each_position[1]))       
        marker_id = each_position_id.id
        maps.event.addListener(marker, 'click', 'myobj.markerOver')
        info = maps.InfoWindow({
            'content':str(each_position[0])+'\t'+str(each_position[1])+'\t'+each_position[2]+'\t'+each_position[3]+'\t'+each_position[4]+'\n'+each_position[5]+'\t'+str(each_position[6])+'\n'+str(each_position[7])+'\t'+"<a href=detail/%s >More Info</a>"%(marker_id),
            'disableAutoPan': True,
            'shadow': 1,
        })
        info.open(gmap, marker)
        maps.event.addListener(info,'click','myobj.infoOver')

    extra_context = {}
    extra_context['form'] = MapForm(initial={'map': gmap})
    return render_to_response('index.html', extra_context, context_instance=RequestContext(request))

""" this method is for showing all detail in a page"""

def detail_info(request , each_position_id):
    ci=RequestContext(request)
    Template_name='detail.html'
    detail_value=Project_title.objects.filter(id=each_position_id)
    print detail_value
    return render_to_response(Template_name,{'detail_value':detail_value},ci)




