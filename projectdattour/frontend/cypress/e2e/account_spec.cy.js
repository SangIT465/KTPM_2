describe('Đăng ký tài khoản', () => {
  it('Đăng ký thành công', () => {
    cy.visit('http://localhost:8000/accounts/register/')
    cy.get('input[name="username"]').type('vsang')
    cy.get('input[name="email"]').type('transang040605@gmail.com')
    cy.get('input[name="password1"]').type('sang12345') // kiểm tra lại name thực tế
    cy.get('input[name="password2"]').type('sang12345') // kiểm tra lại name thực tế
    cy.get('button[type="submit"]').click()
    // Kiểm tra thông báo hoặc url chuyển hướng sau đăng ký thành công
    cy.url().should('include', '/accounts/login/') // hoặc kiểm tra thông báo khác
  })
})

describe('Đăng nhập tài khoản', () => {
  it('Đăng nhập thành công', () => {
    cy.visit('http://localhost:8000/accounts/login/')
    cy.get('input[name="username"]').type('vsang')
    cy.get('input[name="password"]').type('sang12345')
    cy.get('button[type="submit"]').click()
    // Kiểm tra url chuyển hướng hoặc tên user
    cy.url().should('include', '/') // hoặc cy.contains('testuser123').should('exist')
  })

 
})