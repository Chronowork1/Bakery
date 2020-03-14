import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {FaFacebook, FaYoutube, FaTwitter, FaInstagram} from 'react-icons/fa';
import Wheatbread from './Wheatbread.jpg';
import Baguette from './Baguette.jpg';
import Brioche from './Brioche.jpg';
import Cornbread from './Cornbread.jpg';
import Bananabread from './Bananabread.jpg';
import Pitabread from './Pitabread.jpg';

class App extends React.Component {
  render() {
  return (
    <div className="App">
      <html>
        <head>
        </head>
        <body>
          <header id="header">
            <div id="nav">
              <a href="https://www.google.com/">Bread Gallery</a>
              <a href="https://www.google.com/">About</a>
              <a href="https://www.google.com/">Recipes</a>
            </div>
          </header>
          <div class="text-center">
            <h1>Razzi's Bakery</h1>
          </div>
          <div>

          </div>
          <div class="container">
            <div class="row">
              <div class="col-sm-4">
                <h1>Plain Wheat Bread</h1>
                <img src= {Wheatbread} alt="This is a wheat bread."/>
              </div>
              <div class="col-sm-4">
                <h1>Baguette</h1>
                <img src={Baguette} alt="This is a Baguette."/>
              </div>
              <div class="col-sm-4">
                <h1>Pita Bread</h1>
                <img src={Pitabread} alt="This is Pita bread."/>
              </div>
            </div>
            <div class ="row">
              <div class="col-sm-4">
                <h1>Brioche</h1>
                <img src={Brioche} alt="This a Brioche."/>
              </div>
              <div class="col-sm-4">
                <h1>Banana Bread</h1>
                <img src={Bananabread} alt="This is Banana bread"/>
              </div>
              <div class="col-sm-4">
                <h1>Cornbread</h1>
                <img src={Cornbread} alt="This is Cornbread"/>
              </div>
            </div>
          </div>
        </body>
        <footer>
          <h6>Razzi's Bakery</h6>
          <FaFacebook />
          <FaYoutube />
          <FaInstagram />
          <FaTwitter/>
        </footer>
      </html>
    </div>
  );
  }
}

export default App;
