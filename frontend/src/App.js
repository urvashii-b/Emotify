import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Bgm from './components/bgm.mp4';

function Garlic(){
    return(
        <div>
            <nav class="navbar navbar-expand-lg navbar-light bg-dark" style={{paddingLeft:"20px"}}>
            <h1 class="navbar-brand" className="logo" href="#">ANKH</h1>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" id="home" href="http://localhost:3000/home">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" id="abt-us" href="http://localhost:3000/about">About-Us</a>
                </li>
                </ul>
            </div>
            </nav>
            <video loop autoPlay muted id="myvideo">
                <source src={Bgm}></source>
            </video>
            <div>
                <h1 id="abt">Introducing Emotify</h1>
                <p id="abt2"><center>We’ve trained a model called Emotify which reads facial Expressions <br></br>and plays songs to lighten the mood.</center></p>
            </div>
            <a href="http://127.0.0.1:5000/" id="abt3" target="_blank">Try Emotify</a>
        </div>
    );
}

export default Garlic;

//C:\Users\urvas\OneDrive\Desktop\Arithemania-2.0\Emotify_ANKH-master\public\app.py