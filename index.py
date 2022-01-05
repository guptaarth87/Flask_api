{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bfbfea05",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "from flask import jsonify\n",
    "from home import home_bp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e8da0470",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "@app.route('/hello/', methods=['GET', 'POST'])\n",
    "def welcome():\n",
    "    return \"Hello User!\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "73c2f948",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/<string:name>/')\n",
    "def hello(name):\n",
    "    return \"Hello \" + name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "91985151",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/<int:number>/')\n",
    "def incrementer(number):\n",
    "    return \"Incremented number is \" + str(number+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "12b36f85",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/person/')\n",
    "def hello1():\n",
    "    return jsonify({'name':'Arth gupta',\n",
    "                    'address':'India'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f85e3e8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def appRun():\n",
    "  if __name__ == '__main__':\n",
    "    app.run(host='0.0.0.0', port=105)\n",
    "  else:\n",
    "      app.logger.error('This is an ERROR message')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bb670f81",
   "metadata": {},
   "outputs": [],
   "source": [
    "app.register_blueprint(home_bp, url_prefix='/home')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2480430",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__' (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on all addresses.\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      " * Running on http://192.168.1.8:105/ (Press CTRL+C to quit)\n",
      "192.168.1.8 - - [05/Jan/2022 21:27:24] \"GET / HTTP/1.1\" 404 -\n",
      "192.168.1.8 - - [05/Jan/2022 21:27:25] \"GET /favicon.ico HTTP/1.1\" 308 -\n",
      "192.168.1.8 - - [05/Jan/2022 21:27:25] \"GET /favicon.ico/ HTTP/1.1\" 200 -\n",
      "192.168.1.8 - - [05/Jan/2022 21:27:52] \"GET /hello/ HTTP/1.1\" 200 -\n",
      "192.168.1.8 - - [05/Jan/2022 21:27:53] \"GET /favicon.ico/ HTTP/1.1\" 200 -\n",
      "192.168.1.8 - - [05/Jan/2022 21:28:07] \"GET /arth/ HTTP/1.1\" 200 -\n",
      "192.168.1.8 - - [05/Jan/2022 21:28:07] \"GET /favicon.ico/ HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "appRun()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7712a9f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
