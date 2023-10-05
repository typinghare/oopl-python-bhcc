from box import Box
from container import Container
from port import Port
from ship import Ship

# Create a Box of 100 Televisions
television_box = Box("Sony OLED 55 inch BRAVIA XR A80L Series 4K Ultra HD TV", 100)
# Create a Container and Put the Televisions in the Box
television_container = Container()
television_container.box_list.append(television_box)
# Create a MSC Irina Ship.
# This ship flies under the Liberia Flag
# and can hold up to 24,346 containers!
irina = Ship("MSC Irina", "Liberia", 24346)
# Add the container to the MSC Irina
irina.container_list.append(television_container)
# Create the Port of Seattle, which has a max depth of 15 meters.
seattle = Port("Port of Seattle", 15)
# Add the MSC Irina to the Port of Seattle
seattle.ships_in_port.append(irina)

print(television_box)
print(irina)
print(seattle)
