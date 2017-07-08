import turtle
import random

# Tạo đối tượng
bob = turtle.Turtle()
# Tạo hình dạng 'turtle'
bob.shape('turtle')
# Tạo màu
bob.fillcolor('red')
# Tạo vị trí /bob.goto(0,100)/bob.setposition(0,100)
bob.setpos(0,100)
# Xóa dấu vết của đối tượng để lại
bob.clear()
# Trả về 1 góc tạo từ hướng đi của con rùa với đoạn thẳng nối từ
# con rùa đến vị trí đã truyền
c = bob.towards(10,120)
# Trả về khoảng cách từ con rùa đến vị trí đã truyền
d = bob.distance(10,120)
# Tạo hướng đi của con rùa /bob.setheading(0)
bob.seth(180)
# Trả về hướng đi của con rùa hiện tại
head = bob.heading()
# Thay đổi đơn vị đo góc của hình tròn(mặc định hình tròn sẽ có 360 độ)
# Công thức: góc ban đầu /(360/góc sau khi đổi)
bob.degrees(90)
# Thay đổi từ độ sang radian
# bob.radians()
# Không vẽ khi di chuyển /bob.penup()/bob.pu()
bob.up()
# Vẽ khi di chuyển /bob.pendown()/bob.pd()
bob.down()
# Trả về True nếu là down và ngược lại
bob.isdown()
# Tạo bút vẽ: shown là có hiện con rùa hay ko,
bob.pen(shown = True, resizemode = 'auto', outline = 1, tilt = 0, stretchfactor = (1,1))
# Lát cắt của hình, có thể âm hoặc dương
bob.shearfactor(1)
# Xoay rùa từ góc độ nghiêng hiện tại, ko làm thay đổi hướng
bob.tilt(30)
# Xoay rùa theo góc đã cho, bất kể góc hiện tại, ko làm thay đổi hướng
bob.settiltangle(30)
# Set hoặc trả lại ma trận chuyển đổi hiện tại của con rùa.
bob.shapetransform()
# Gọi trước khi vẽ hình
bob.begin_fill()
# Tiến về trước 1 khoảng cách /bob.forward(100)
bob.fd(100)
# Rẽ trái 1 góc bao nhiêu /bob.left(90)
bob.lt(90)
# Tạo độ trễ theo mili giây
turtle.delay(10)
# Lùi về sau 1 khoảng cách /bob.back(100)/bob.backward(100)
bob.bk(100)
# Rẽ phải 1 góc bao nhiêu /bob.right(90)
bob.rt(90)
# Vẽ 1 dấu chấm với đường kính và màu
bob.dot(10, 'yellow')
# Sao chép hình dạng của đối tượng (và gán lun id để tiện xóa)
a = bob.stamp()
# Xóa hình đã sao chép dựa vào id
bob.clearstamp(a)
bob.fd(100)
# Hủy hành động trước đó của đối tượng
bob.undo()
# Xóa n hình đã sao chép từ đầu/cuối(<0), nếu ko có tham số thì xóa hết
bob.clearstamps(-2)
# Đưa con rùa về vị trí (0,0) và hướng 0 độ
bob.home()
# Nếu ko có steps(tham số 3rd) thì vẽ hình tròn, nếu có thì số steps 
# tương ứng với số cạnh đa giác được vẽ, tham số 1st(radius)là bán kính,
# tham số 2nd(extend) là mở rộng góc bao nhiêu độ, 180 là nửa vòng tròn
bob.circle(120,360,10)
# Gọi khi kết thúc vẽ
bob.end_fill()
# Xóa các hình vẽ, quay lại điểm 0,0 và đặt các biến về giá trị mặc định.
bob.reset()
# Tạo tốc độ chạy /bob.speed(9)
bob.speed('fast')
# Dừng màn hình để xem
turtle.mainloop()