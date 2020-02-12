import responder
from services.api.deadman_switch_api import DeadmanSwitchHealth

api = responder.API(
    title = "Deadman Switch Board",
    version = "0.1.0"
)

api.add_route("/health", DeadmanSwitchHealth)

if __name__ == '__main__':
    api.run()
