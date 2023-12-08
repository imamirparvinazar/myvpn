import vpn

kwargs = dict(
    vpn_username="myusername",
    vpn_password="Mypassword23$"
)

vpn_server = vpn.VPNServer(**kwargs)

# Create a VPN Server
vpn_server.create_vpn_server()
