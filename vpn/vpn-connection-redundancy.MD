## This is how you add redundancy to your VPN connection
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html#VPNConnections

sing Redundant VPN Connections to Provide Failover
As described earlier, a VPN connection has two tunnels to help ensure connectivity in case one of the VPN connections becomes unavailable. To protect against a loss of connectivity in case your customer gateway becomes unavailable, you can set up a second VPN connection to your VPC and virtual private gateway by using a second customer gateway. By using redundant VPN connections and customer gateways, you can perform maintenance on one of your customer gateways while traffic continues to flow over the second customer gateway's VPN connection. To establish redundant VPN connections and customer gateways on your remote network, you need to set up a second VPN connection. The customer gateway IP address for the second VPN connection must be publicly accessible.

The following diagram shows the two tunnels of each VPN connection and two customer gateways.


Dynamically routed VPN connections use the Border Gateway Protocol (BGP) to exchange routing information between your customer gateways and the virtual private gateways. Statically routed VPN connections require you to enter static routes for the remote network on your side of the customer gateway. BGP-advertised and statically entered route information allow gateways on both sides to determine which tunnels are available and reroute traffic if a failure occurs. We recommend that you configure your network to use the routing information provided by BGP (if available) to select an available path. The exact configuration depends on the architecture of your network.
