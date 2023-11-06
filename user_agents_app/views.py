from django.shortcuts import render
from django_user_agents.utils import get_user_agent

def indexed(req):
    return render(req,"user_agents_app/index.html")


def info_agent(req):
    user_agent = get_user_agent(req)
    return render(req,"user_agents_app/info.html" , {"info":user_agent})


def get_agent(req):
    user_agent = get_user_agent(req)
    client_ip = req.META.get('REMOTE_ADDR')
    host_name = req.META.get('HTTP_HOST')
    if user_agent.is_mobile:
        info_txt = f'Estas usando un movil con host {host_name} e ip {client_ip}. '
        if user_agent.is_touch_capable:
            info_txt += "El dispositivo es tactil"
        else:
            info_txt += "El dispositivo no es tactil"

    elif user_agent.is_pc:
        info_txt = f'Estas usando un PC con host {host_name} e ip {client_ip}. '
        if user_agent.is_touch_capable:
            info_txt += "El dispositivo es tactil"
        else:
            info_txt += "El dispositivo no es tactil"
        
    elif user_agent.is_tablet:
        info_txt = f'Estas usando una Tablet con host {host_name} e ip {client_ip}. '
        if user_agent.is_touch_capable:
            info_txt += "El dispositivo es tactil"
        else:
            info_txt += "El dispositivo no es tactil"
       
    elif user_agent.is_bot:
        info_txt = f'Estas usando un bot con host {host_name} e ip {client_ip}. '
        if user_agent.is_touch_capable:
            info_txt += "El dispositivo es tactil"
        else:
            info_txt += "El dispositivo no es tactil"

    return render(req, "user_agents_app/info_dispositivo.html" , {"info_txt": info_txt})