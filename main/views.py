from django.shortcuts import render
from .models import Wilaya, Commune, Route, Section, Campagne, BruteData, Traffic

def dashboard_view(request):
    wilayas = Wilaya.objects.all()
    communes = Commune.objects.all()
    routes = Route.objects.all()
    sections = Section.objects.all()
    campagnes = Campagne.objects.all()

    # Get selected filters from query parameters
    selected_wilaya = request.GET.get("wilaya")
    selected_commune = request.GET.get("commune")
    selected_route = request.GET.get("route")
    selected_section = request.GET.get("section")
    selected_campagne = request.GET.get("campagne")

    filtered_data = BruteData.objects.all()

    if selected_section:
        filtered_data = filtered_data.filter(section_id=selected_section)
    elif selected_commune:
        filtered_data = filtered_data.filter(section__commune_id=selected_commune)
    elif selected_wilaya:
        filtered_data = filtered_data.filter(section__commune__wilaya_id=selected_wilaya)

    if selected_route:
        filtered_data = filtered_data.filter(section__route_id=selected_route)

    if selected_campagne:
        filtered_data = filtered_data.filter(campagnes__id=selected_campagne)

    traffic_data = Traffic.objects.filter(id__in=filtered_data)

    return render(request, "dashboard.html", {
        "wilayas": wilayas,
        "communes": communes,
        "routes": routes,
        "sections": sections,
        "campagnes": campagnes,
        "traffic_data": traffic_data,
    })
