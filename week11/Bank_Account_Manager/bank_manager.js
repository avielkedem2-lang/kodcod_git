import {save, searchCustomer} from "./customer_manager.js"

export function deposit(id, amount, customer){
    const theCustomer = customer
    theCustomer.balance += amount
}


export function Withdraw(id, amount, customer){
    const theCustomer = customer
    theCustomer.balance -= amount
}


export function showStatistics(){
    let listCustomers = save.getAllCustomers()
    return {
        Total_Customers: listCustomers.length,
        Active_Accounts: listCustomers.filter((customer) => {return customer.isActive}).length,
        Total_Money: listCustomers.reduce((total, customer) => {return total + customer.balance}, 0),
        Average_Balance: listCustomers.reduce((total, customer) => {return total + customer.balance}, 0) / listCustomers.length,
        Highest_Balance: listCustomers.sort((a,b) => b.balance - a.balance)[0].balance
    }
}


// const accountsList = [
//   {
//     id: "1",
//     fullName: "John Doe",
//     accountType: "Checking",
//     balance: 5000,
//     isActive: true
//   },
//   {
//     id: "2",
//     fullName: "Jane Smith",
//     accountType: "Savings",
//     balance: 12500,
//     isActive: true
//   },
//   {
//     id: "3",
//     fullName: "Alex Jones",
//     accountType: "Business",
//     balance: 850,
//     isActive: false
//   }
// ];
// console.log(showStatistics())
