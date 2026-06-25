




export function createId() {
  let id = 0
  function increment() {
    return ++id
  }
  return increment
}



export function createCustomer(id, name, accountType, balance) {
  const newCustomer = {
    id: id,
    fullName: name,
    accountType: accountType,
    balance: balance,
    isActive: true
  }
  return newCustomer
}



export function saveCustomer() {
  let customers = []
  function addCustomer(customer) {
    customers.push(customer)
  }
  function getAllCustomers(){
    console.log(customers)
  }
return {addCustomer, getAllCustomers}
}





// const inc = createId()
// const cus = saveCustomer()
// cus.addCustomer(createCustomer(inc(),"avi", null, 90))
// cus.addCustomer(createCustomer(inc(),"moshe", null, 333))
// cus.getAllCustomers()






