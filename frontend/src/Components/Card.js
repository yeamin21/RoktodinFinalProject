import { Component } from "react";
import "./Card.scss"
export default class Card extends Component{
    constructor(props) {
        super(props)
    
        this.state = {
             item: props.item
        }
    }
    
    render(){
        const {receiver}  = this.state.item
        return(<div className='card'>{receiver}</div>)
    }
}