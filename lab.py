class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """เพิ่มข้อมูลเข้า stack"""
        self.items.append(item)

    def pop(self):
        """ลบและคืนค่าข้อมูลบนสุด"""
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def peek(self):
        """คืนค่าข้อมูลบนสุดโดยไม่ลบออก"""
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

    def is_empty(self):
        """ตรวจสอบว่า stack ว่างหรือไม่"""
        return len(self.items) == 0

    def size(self):
        """คืนค่าจำนวนสมาชิกใน stack"""
        return len(self.items)