describe('Đặt tour', () => {
  it('Đặt tour thành công', () => {
    cy.visit('http://localhost:8000/bookings/tour/1/date/1/')
    cy.get('input[name="full_name"]').type('Nguyễn Văn A')
    cy.get('input[name="email"]').type('test@example.com')
    cy.get('input[name="phone"]').type('0123456789')
    cy.get('input[name="address"]').type('Hà Nội')
    cy.get('input[name="adults"]').clear().type('2')
    cy.get('input[name="children"]').clear().type('0')
    cy.get('button[type="submit"]').click()
    cy.contains('Xác nhận đặt tour')
  })
})