from waitress import serve
import RestController
serve(RestController.app, host='0.0.0.0', port=8080)