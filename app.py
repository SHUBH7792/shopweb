from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

# Uploads folder path (for PDFs, etc.)
app.config['UPLOAD'] = os.path.join(app.root_path, 'uploads')

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD'], exist_ok=True)

# --- Routes ---

@app.route('/')
def helloworld():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/classicaldiya')
def product():
    images = {
        "4 PIECE DIYA SET": [
            '4pc1.png', '4pc2.jpg', '4pc3.jpg', '4pc4.jpg', '4pc5.jpg',
            '4pc6.jpg', '4pc7.jpg', '4pc8.png', '4pc9.png', '4pc10.png'
        ],
        "12 PIECE BOX SET": [
            '12box1.jpg', '12box2.jpg', '12box3.jpg', '12box4.jpg', '12box5.jpg',
            '12box6.jpg', '12box7.jpg', '12box8.jpg', '12box9.jpg', '12box10.jpg'
        ],

         "4 PIECE MATKI SET": [
            '4mat1.jpg', '4mat2.jpeg', '4mat3.jpg', '4mat4.jpg', '4mat5.jpg',   
            '4mat6.jpg', '4mat7.jpg', '4mat8.jpg', '4mat9.jpg', '4mat10.jpg'  
        ],

         "7 PIECE MATKI SET": [
            '7mat1.jpg', '7mat2.jpg', '7mat3.jpg', '7mat4.jpg', '7mat5.jpg',   
            '7mat6.jpg', '7mat7.jpg', '7mat8.jpg', '7mat9.jpg', '7mat10.jpg'  
        ],

        "AKHAND DIYA": [
            'ak1.png', 'ak2.png', 'ak3.png', 'ak4.png',
            'ak5.png', 'ak6.png', 'ak7.png', 'ak8.png',
            'ak9.png', 'ak10.png'
        ]
    }    
    return render_template('class.html', images = images)

@app.route('/cateringgood')
def product2():
    images = {
        "CUPS": [
            'c1.jpg', 'c2.jpg', 'c3.jpg', 'c4.jpg', 'c5.jpg',
            'c6.jpg', 'c7.jpg', 'c8.jpg', 'c9.jpg', 'c10.jpg',
        ],
         "HANDI": [
            'h1.jpg', 'h2.jpg', 'h3.jpg', 'h4.jpg', 'h5.jpg',
            'h6.jpg', 'h7.jpg', 'h8.jpg', 'h9.jpg', 'h10.jpg',
        ],
        "matka": [
            'b1.jpg', 'b2.jpg', 'b3.jpg', 'b4.jpg', 'b5.jpg',
            'ma2.jpg', 'ma4.jpg', 'ma1.jpg', 'ma4.jpg', 'ma3.jpg',
        ]
     }
    return render_template('cat.html', images = images)

@app.route('/newarrivals')
def newprod():
    images = {
        "pre": [
            'p1.png', 'p2.png', 'p3.png', 'p4.jpeg', 'p5.jpeg',
            'p6.jpeg', 'c7.jpg', 'c8.jpg', 'c9.jpg', 'c10.jpg',
        ],
     }
    return render_template('newpro.html', images = images)


# --- PDF Handling ---

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD'], filename, as_attachment=True)

@app.route('/view/<filename>')
def view_pdf(filename):
    return send_from_directory(app.config['UPLOAD'], filename, as_attachment=False)

# --- Main Entry ---

if __name__ == '__main__':
    app.run(debug=True)
