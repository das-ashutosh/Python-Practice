import random
import time
class Packet:
    def __init__(self, packet_id, source, destination, data):
        self.packet_id = packet_id
        self.source = source
        self.destination = destination
        self.data = data
        self.status = "Created"

    def transmit(self):
        print(f"\nPacket #{self.packet_id}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Data: {self.data}")

        self.status = "In Transit"
        print("Status: Sending packet...")

        time.sleep(0.5)

        # Simulate a 90% delivery success rate
        if random.random() < 0.9:
            self.status = "Delivered"
            print("Status: Delivered successfully!")
        else:
            self.status = "Lost"
            print("Status: Packet lost!")

        return self.status


def main():
    packets = []

    print("===== NETWORK PACKET SIMULATOR =====")

    try:
        count = int(input("How many packets should be sent? "))

        if count <= 0:
            print("Enter a positive number.")
            return

        source = input("Enter source address: ").strip()
        destination = input("Enter destination address: ").strip()

        if not source or not destination:
            print("Addresses cannot be empty.")
            return

        for packet_id in range(1, count + 1):
            data = input(f"Enter data for packet {packet_id}: ")

            packet = Packet(
                packet_id, source, destination, data
            )
            packets.append(packet)
            packet.transmit()

        delivered = sum(
            packet.status == "Delivered" for packet in packets
        )
        lost = sum(
            packet.status == "Lost" for packet in packets
        )

        print("\n===== NETWORK REPORT =====")
        print(f"Total packets: {len(packets)}")
        print(f"Delivered: {delivered}")
        print(f"Lost: {lost}")
        print(f"Delivery rate: {delivered / len(packets) * 100:.1f}%")

    except ValueError:
        print("Please enter a valid whole number.")


if __name__ == "__main__":
    main()
```
