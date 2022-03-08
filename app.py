from flask import Flask, render_template
import dataElaboration 

app= Flask(__name__)

dataToRender=dataElaboration.expenses
dataElaboration.openData()

@app.route('/', methods=['GET', 'POST'])
def index():
    dataElaboration.retrieveData()
    groceryCost=dataElaboration.costGrocery()
    shoppingCost=dataElaboration.costShopping()
    entertainmentCost=dataElaboration.costEntertainment()
    healthCost=dataElaboration.costHealth()
    transportCost=dataElaboration.costTransport()
    homeCost=dataElaboration.costHome()
    spent=dataElaboration.spent()
    return render_template(
        'index.html', 
        data=dataToRender,
        grocery=groceryCost,
        shopping=shoppingCost,
        entertainment=entertainmentCost,
        health=healthCost,
        transport=transportCost,
        home=homeCost,
        moneySpent=spent
        )


if __name__ =="__main__":
    app.run(debug=True)
    #FLASK_APP=app.py flask run                                 