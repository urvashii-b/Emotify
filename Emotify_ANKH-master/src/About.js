import React from "react";
import eye from './components/ankh.png';

function About(){
    return(
        <div style={{color:"white", fontFamily:"cursive", fontSize:"30px", margin:"30px"}}>
            <center><img src={eye} style={{height:"180px", width:"300px"}}></img><h1>ANKH</h1></center>
            <p>This Project focuses on music for all emotions , whether you are happy sad or suffering a heart break <br></br>
                our app doesnt need to be told anything it reads you emotion like a friend and plays a song to sothen your heart.
            </p>
            Team members:
            <ul>
                <li>
                    Urvashi Bhargava
                </li>
                <li>
                    Nishank Koul
                </li>
                <li>
                    Pragya
                </li>
                <li>
                    Shrushti
                </li>
            </ul>

        </div>
    );
}

export default About;