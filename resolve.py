from app import create_app

app = create_app()

# Limiter(app, key_func=get_remote_address(), default_limits=["200 per day", "10 per minute"])

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'], host=app.config['HOST'])
