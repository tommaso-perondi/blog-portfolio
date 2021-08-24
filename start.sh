export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
export SQLALCHEMY_DATABASE_URI=sqlite:///sqlite.db
export SECRET_KEY="umxnpf_@dwaq@0*@-=@p$e7ou#*5*a(p*)%n$i6pgx16cgi1@6"
python -m flask run -h 0.0.0.0
