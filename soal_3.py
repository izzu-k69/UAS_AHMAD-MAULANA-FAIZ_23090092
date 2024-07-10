from queue_restoran import QueueRestoran

if __name__ == "__main__":
    queue = QueueRestoran()

    queue.enqueue("Nasi Goreng")
    queue.enqueue("Soto Ayam")
    queue.enqueue("Es Teh Manis")

    queue.dequeue()
    queue.enqueue("Mie Ayam")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
