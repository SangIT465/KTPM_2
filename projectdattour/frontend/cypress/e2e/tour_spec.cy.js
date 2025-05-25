describe('Tour - Danh sách và chi tiết', () => {
  it('Tìm kiếm tour', () => {
    const keyword = encodeURIComponent('Đà Nẵng')
    cy.visit(`http://localhost:8000/tours/?q=${keyword}`) // Sửa lại URL đúng với backend
    cy.contains('Đà Nẵng').should('exist')
  })

  it('Xem chi tiết tour', () => {
    cy.visit('http://localhost:8000/tours/')
    cy.get('.tour-card a').first().click() // Sửa selector cho đúng với HTML của bạn
    cy.get('h1.title').should('exist')     // Sửa selector cho đúng với HTML của bạn
  })
})