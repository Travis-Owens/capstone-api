
import falcon

class print_x_real_ip(object):
    def process_request(self, req, resp):
        # Retreives the end-user IP address from the header appened by NGINX
        print(req.get_header('x-real-ip'))
