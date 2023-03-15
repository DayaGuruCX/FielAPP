import React from 'react';

import BotonHeader from '../BotonHeader'

import btn2 from "../../../Assests/imagenes/btn2.png";
import btn3 from "../../../Assests/imagenes/btn3.png";
import btn4 from "../../../Assests/imagenes/btn4.png";
import styles from "../../../Assests/css/header/mobile/headermobile.module.scss"
import Titulo from './Titulo';
class Header extends React.Component{
    render(){
        return(
            <div className={styles.estiloHeaderMobile}>   
                <div className={styles.contenedorEspacio}></div>
                <div className={styles.contenedorBotonesMobile}>
                    <div className={styles.contbotonMobile}>
                        <BotonHeader src={btn2}></BotonHeader>
                    </div>
                    <div className={styles.contbotonMobile}>
                        <BotonHeader src={btn3}></BotonHeader>
                    </div>
                    <div className={styles.contbotonMobile}>
                        <BotonHeader src={btn4}></BotonHeader>
                    </div>
                </div>  
                <div className={styles.contenedorTitulo}>
                    <Titulo tit={"Seccion Seleccionada"}></Titulo>
                </div>   
            </div>
        );
    
    }
}
export default Header;