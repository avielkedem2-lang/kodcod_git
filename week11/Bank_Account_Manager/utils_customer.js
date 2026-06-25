import {createCustomer, searchCustomer} from "./customer_manager.js"
import rl from "readline-sync"


function nameValidation(name){
    if (name){
        return true
    }
    return false
}


function accountTypeValdation(accountType){
    const onlyTypeAccount = ["Regular", "Premium", "Student"]
    return onlyTypeAccount.find((val) => {
        return accountType.toLowerCase() === val.toLowerCase()
    })
}


function balanceValdation(balance){
    if (balance >= 0){
        return true
    }
    return false
}



export function sendToCreateCustomer(id){
    const name = rl.question("Enter your name: ");
    if (nameValidation(name)){
        const accountType = rl.question("Enter your type account: ");

        if (accountTypeValdation(accountType)){
            const balance = rl.questionInt("Enter your balance: ");

            if (balanceValdation(balance)){
                return createCustomer(id, name, accountType, balance)
            }
            else {
                console.log("balance most to be 0 or more")
            }

        }
        else{
            console.log(`account cna't be ${accountType}`)
        }
    }
    else{
        console.log( "name most to be a word")
    }
}




export function sandToSearchCustomer(){
    const val = rl.question("Enter id or name for the search: ")
    if (nameValidation(val)){
        const customer = searchCustomer(val)
        if (customer){
            return customer
        }else {
            console.log(`The value= ${val} not fond!`)
            return false
        }
    }else{
        console.log("name or id most to be a word or number")
        return false
    }
}