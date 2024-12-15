import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='akldjlkdajf;kladsjkfl')
toado = gmaps.geocode('DHGTVT')
reverse_geocode = gmaps.reverse_geocode(toado)
now = datetime.now()
direction = gmaps.directions("hanoi","noibai", mode="transit", departure_time=)


from geoip import geolite2
result = geolite2.lookup(ipaddress)
if result is not None:
    print("country: ",result.country)
    result.continent
    result.timezone
    
import dnspython
dnspython.resolver

result = dnspython.resolver.query('www.abc.com','A')
for i in result:
    print("IP:",i.to_text(l))