import { useState, useEffect } from "react";
import { Link } from "react-router-dom";


function ItemList(props){
    return(
        <div className="col">
            {props.list.map(data =>{
                const item = data.item;
                return(
                    <div key={item.id} className="item-card">
                        <img src={item.img} className= "item-image" />
                        <div className="card-body">
                            <h3>{item.name}</h3>
                            <p>Collection: {item.collection}</p>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

export default function Home(){

    return (
        <>
        <section className="hero-container">
            <div className="hero">
                <h1>Crossing Mulholland</h1>
            </div>
        </section>
        <section className="suggested-items">
            
        </section>
        </>
    )
};
