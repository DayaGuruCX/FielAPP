import React from 'react';

import {Link} from "react-router-dom";

import IconoMenu from './IconoMenu'

import img1 from "../../Assests/imagenes/Plan.png";
import img2 from "../../Assests/imagenes/Premios.png";
import img3 from "../../Assests/imagenes/Redimir.png";
import img4 from "../../Assests/imagenes/estadísticas.png";

import styles from "../../Assests/css/laterales/lateralIzq.module.scss"
import TextosMenuIzq from './TextosMenuIzq';
class LateralIzq extends React.Component{
    render(){
        return(
            <div className={styles.estiloLaterales}>  
                <div className={styles.contmenu}>
                    <div className={styles.linea}>
                        <div className={styles.conticono}>
                            <IconoMenu src={img4}/>
                        </div>
                        <div className={styles.conttexto}>
                            <Link to="estadisticas" style={{ textDecoration: 'none' }}><TextosMenuIzq txt="Estadísticas" id="estadistica"/></Link>
                        </div>
                    </div>
                    <div className={styles.linea}>
                        <div className={styles.conticono}>
                            <IconoMenu src={img3}/>
                        </div>
                        <div className={styles.conttexto}>
                            <Link to="redimir" style={{ textDecoration: 'none' }}><TextosMenuIzq txt="Redimir" id="redimir"/></Link>
                        </div>
                    </div>
                    <div className={styles.linea}>
                        <div id="Pemios" className={styles.conticono}>
                            <IconoMenu src={img2}/>
                        </div>
                        <div className={styles.conttexto}>
                            <Link to="premios" style={{ textDecoration: 'none' }}><TextosMenuIzq txt="Premios FIEL" id="premios"/></Link>
                        </div>
                    </div>
                    <div className={styles.linea}>
                        <div className={styles.conticono}>
                            <IconoMenu src={img1}/>
                        </div>
                        <div id="Plan" className={styles.conttexto}>
                            <Link to="miplan" style={{ textDecoration: 'none' }}><TextosMenuIzq txt="Mi Plan" id="plan"/></Link>
                        </div>
                    </div>
                </div>    
            </div>
        );
    
    }
}
export default LateralIzq;