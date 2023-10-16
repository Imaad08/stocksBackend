import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from pandas_datareader import data as pdr
import plotly.graph_objs as go

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class StockData(Resource):
    def get(self):
        stock_tickers = request.args.get('stock_tickers').split(',')

        stock_data = []
        for ticker in stock_tickers:
            df = pdr.DataReader(ticker, 'yahoo', period="1y")
            stock_data.append({
                'ticker': ticker,
                'data': df.to_dict(orient='records')
            })

        plot_data = []
        for stock in stock_data:
            trace = go.Scatter(x=[d['Date'] for d in stock['data']],
                               y=[d['Close'] for d in stock['data']],
                               mode='lines',
                               name=stock['ticker'])
            plot_data.append(trace)

        graph = json.dumps(plot_data, cls=plotly.utils.PlotlyJSONEncoder)

        table_data = []
        for stock in stock_data:
            table_data.append({
                'Ticker': stock['ticker'],
                'Data': stock['data']
            })

        return jsonify({'graph': graph, 'table': table_data})


api.add_resource(StockData, '/stock_data')

