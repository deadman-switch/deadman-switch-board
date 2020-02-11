import responder

api = responder.API()


@api.route("/health")
async def greet_world(req, resp):
    resp.text = f"host healthy"

if __name__ == '__main__':
    api.run()
