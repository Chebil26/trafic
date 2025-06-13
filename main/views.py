from django.shortcuts import render
from .models import Wilaya, Commune, Route, Section, Campagne, BruteData, Traffic

def dashboard_view(request):
    wilayas = Wilaya.objects.all()
    routes = Route.objects.all()
    sections = Section.objects.all()
    campagnes = Campagne.objects.all()

    # Filter data (basic version - can be improved with QueryDicts)
    selected_wilaya = request.GET.get("wilaya")
    selected_route = request.GET.get("route")
    selected_section = request.GET.get("section")
    selected_campagne = request.GET.get("campagne")

    filtered_data = BruteData.objects.all()
    if selected_section:
        filtered_data = filtered_data.filter(section_id=selected_section)

    traffic_data = Traffic.objects.filter(id__in=filtered_data)

    return render(request, "dashboard.html", {
        "wilayas": wilayas,
        "routes": routes,
        "sections": sections,
        "campagnes": campagnes,
        "traffic_data": traffic_data,
    })
