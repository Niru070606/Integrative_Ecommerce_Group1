from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('public/main.html')

@app.route('/secondPage')
def secondPage():
    
    products = [

    {
        "howMany": "howMany1",
        "showHowMany": "p1",
        "qty": "qty1",
        "imageFilename": "IMAGES_VIDEOS/gaminglaptop.avif",
        "productName": "MSI Cyborg 15",
        "description": "High performance for gaming and work",
        "price": "₱85,999",
    },
    {
        "howMany": "howMany2",
        "showHowMany": "p2",
        "qty": "qty2",
        "imageFilename": "IMAGES_VIDEOS/gamingphone.jpg",
        "productName": "Asus ROG Phone",
        "description": "Latest Android flagship\nphone",
        "price": "₱35,000",
    },
    {
        "howMany": "howMany3",
        "showHowMany": "p3",
        "qty": "qty3",
        "imageFilename": "IMAGES_VIDEOS/wirelessheadphone.jpg",
        "productName": "RGB Gaming Headphone",
        "description": "Noise cancelling\nheadphones",
        "price": "₱5,000",
    },
    {
        "howMany": "howMany4",
        "showHowMany": "p4",
        "qty": "qty4",
        "imageFilename": "IMAGES_VIDEOS/smartwatch.jpg",
        "productName": "Garmin Venu Smartwatch",
        "description": "Track your fitness\nand health",
        "price": "₱8,500",
    },
    {
        "howMany": "howMany5",
        "showHowMany": "p5",
        "qty": "qty5",
        "imageFilename": "IMAGES_VIDEOS/gamingChair.jpg",
        "productName": "ROG Gaming Chair",
        "description": "Stability and\nmore comfortable",
        "price": "₱20,000",
    },
    {
        "howMany": "howMany6",
        "showHowMany": "p6",
        "qty": "qty6",
        "imageFilename": "IMAGES_VIDEOS/gamingkeyboard.avif",
        "productName": "ROG Gaming Keyboard",
        "description": "Pro Accuracy /\nRapid Response",
        "price": "₱7,500",
    },
    {
        "howMany": "howMany7",
        "showHowMany": "p7",
        "qty": "qty7",
        "imageFilename": "IMAGES_VIDEOS/gamingmouse.jpg",
        "productName": "ROG Gaming Mouse",
        "description": "Precision\nthat dominates",
        "price": "₱4,000",
    },
    {
        "howMany": "howMany8",
        "showHowMany": "p8",
        "qty": "qty8",
        "imageFilename": "IMAGES_VIDEOS/gamingcontroller.avif",
        "productName": "Gaming Controller",
        "description": "Play your way\nRule the game",
        "price": "₱6,000",
    },
    {
        "howMany": "howMany9",
        "showHowMany": "p9",
        "qty": "qty9",
        "imageFilename": "IMAGES_VIDEOS/gamingmonitor.jpg",
        "productName": "ROG Gaming Monitor",
        "description": "See it first\nStrike first",
        "price": "₱21,500",
    },
    {
        "howMany": "howMany10",
        "showHowMany": "p10",
        "qty": "qty10",
        "imageFilename": "IMAGES_VIDEOS/mousepad.jpg",
        "productName": "ROG Mousepad",
        "description": "Smooth moves\nBright plays",
        "price": "₱1,000",
    },
    {
        "howMany": "howMany11",
        "showHowMany": "p11",
        "qty": "qty11",
        "imageFilename": "IMAGES_VIDEOS/soomfoncam.jpg",
        "productName": "Soomfon Webcam",
        "description": "Stream\nlike a pro",
        "price": "₱3,000",
    },
]
    return render_template('public/secondPage.html', products=products)

@app.route('/product')
def product():
    return render_template('public/product.html')

@app.route('/deals')
def deals():
    return render_template('public/deals.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/product/<filename>')
def product_detail(filename):
    return render_template('public/product_templates/' + filename + '.html')
"""
yung product/filename route web url
 ay kukunin nya lahat ng name ng file para ma rener yung exact file gamit yung string concatenation sa baba



Use The funcntion as first href parameter and filename as second href parameter
"""

if __name__ == '__main__':
    app.run(debug=True)

