import kivy
kivy.require('1.0.5')

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from ipaddress import ip_network, ip_address


class Controller(GridLayout):

    def change_subnet(self):
        print("change called")
        self.subnet = self.text_input_subnet_no_prefix.text+"/"+self.text_input_subnet_mask.text
        print(self.subnet)
        self.calculate()

    def change_subnet2(self):
        self.subnet = self.text_input_subnet.text.strip()
        if not self.subnet:
            self.subnet = self.text_input_subnet_no_prefix.text+"/"+self.text_input_subnet_mask.text
        self.calculate()
    
    def calculate(self):
        try:
            subnet = ip_network(self.subnet)
            network_part = str(subnet.network_address)
            netmask = str(subnet.netmask)
            ip_list = list(subnet.hosts())
            first_host = str(ip_list[0])
            last_host = str(ip_list[-1])
            broadcast_ip = str(subnet.broadcast_address)
            hostmask = str(subnet.hostmask)
            prefix_len = str(subnet.prefixlen)
            num_addresses = str(subnet.num_addresses)
            self.text_input_subnet_no_prefix.text = network_part
            self.text_input_subnet_mask.text = netmask
            #self.text_input_result.text="network: "+str(network_part)+"\n"+"netmask: "+str(netmask)+"\n"
            self.text_input_network.text = "network:\n"+network_part
            self.text_input_mask.text = "netmask:\n"+netmask
            self.text_input_first_host.text = "first host:\n"+first_host
            self.text_input_last_host.text = "last host:\n"+last_host
            self.text_input_broadcast.text = "broadcast:\n"+broadcast_ip
            self.text_input_num_addresses.text = "number of addresses:\n"+num_addresses
        except Exception as e:
            self.text_input_network.text="not valid subnet "+str(e)


class SubnetCalcApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    SubnetCalcApp().run()