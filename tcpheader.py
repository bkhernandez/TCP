from bitstring import *

class Packet:

    def __init__(self):
        """
        The TCP packet header:

        0                   1                   2                   3
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |          Source Port          |       Destination Port        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                        Sequence Number                        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                    Acknowledgment Number                      |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |  Data |           |U|A|P|R|S|F|                               |
       | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
       |       |           |G|K|H|T|N|N|                               |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |           Checksum            |         Urgent Pointer        |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                    Options                    |    Padding    |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
       |                             data                              |
       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        """

        self.source_port = bytearray(8000)
        self.destination_port = bytearray(8001)
        self.seq_num = bytearray()
        self.ack_num = bytearray()
        self.data_offset = bytearray(5)
        self.reserved = bytearray([0, 0, 0, 0, 0, 0])                   # 6 bits of 0
        self.urg_bit = bytearray()
        self.ack_bit = bytearray()
        self.psh_bit = bytearray()                                      # not used
        self.rst_bit = bytearray()                                      # not used
        self.syn_bit = bytearray()
        self.fin_bit = bytearray()
        self.window_size = bytearray()
        self.checksum = bytearray()
        self.urgent_pointer = bytearray()
        self.data = b'noting yet'                                       # 11776 bits or 1472 bytes

    #Setters

    def set_source_port(self, portnum):
        self.source_port = portnum

    def set_destination_port(self, srcport):
        self.source_port = srcport

    def set_seq_num(self, seqnum):
        self.seq_num = seqnum

    def set_ack_num(self, acknum):
        self.ack_num = acknum

    def set_data_offset(self, doffset):
        self.data_offset = doffset

    def set_readwrite(self, bitval):
        # 1 = read
        # 0 = write
        self.urg_bit = bitval

    def set_ack_bit(self, bitval):
        self.ack_bit = bitval

    def set_syn_bit(self, bitval):
        self.syn_bit = bitval

    def set_fin_bit(self, bitval):
        self.fin_bit = bitval

    def set_window_size(self, winval):
        self.window_size = winval

    def set_checksum(self, checkval):
        self.checksum = checkval

    def set_data(self, data):
        self.data = data

    # Getters

    def get_source_port(self):
        return self.source_port

    def get_destination_port(self):
        return self.destination_port

    def get_seq_num(self):
        return  self.seq_num

    def get_ack_num(self):
        return self.ack_num

    def get_data_offset(self):
        return self.data_offset

    def get_read_write(self):
        return self.urg_bit

    def get_data(self):
        return self.data

    def create_bytearray(self):
        packetarray = bytearray()
        packetarray += self.source_port
        packetarray += self.destination_port
        packetarray += self.seq_num
        packetarray += self.ack_num
        packetarray += self.data_offset
        packetarray += self.reserved
        packetarray += self.urg_bit
        packetarray += self.ack_bit
        packetarray += self.ack_bit
        packetarray += self.psh_bit
        packetarray += self.rst_bit
        packetarray += self.syn_bit
        packetarray += self.fin_bit
        packetarray += self.window_size
        packetarray += self.checksum
        packetarray += self.urgent_pointer
        packetarray += self.data

        return packetarray
