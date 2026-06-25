import {save, searchCustomer} from "./customer_manager.js"

export function deposit(id, amount, customer){
    const theCustomer = customer
    theCustomer.balance += amount
}





