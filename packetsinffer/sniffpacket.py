#!/usr/bin/python

import socket
import os,sys
import struct
import binascii

sock_created = False
sniffer_socket = 0

def analyze_udp_header(data_recv):
	udp_header = struct.unpack('!4H', data_recv[:8])
	src_port = udp_header[0]
	dst_port = udp_header[1]
	length = udp_header[2]
	checksum = udp_header[3]
	data = data_recv[8:]
	print("_____________________UDP HEADER______________________")
	print("Source :%hu " % src_port)
	print("destination %hu " % dst_port)
	print("length %hu " % length)
	print("Check sum %hu " % checksum)
	return data


def analyze_tcp_header(data_recv):
	tcp_hdr = struct.unpack('!2H2I4H',data_recv[:20])
	src_port = tcp_hdr[0]
	dst_port = tcp_hdr[1]
	seq_num = tcp_hdr[2]
	ack_num = tcp_hdr[3]
	data_offset = tcp_hdr[4] >> 12
	reserved = (tcp_hdr[5] >> 6) & 0x03ff
	flags = tcp_hdr[4] & 0x003f
	window = tcp_hdr[5]
	checksum = tcp_hdr[6]
	urg_ptr = tcp_hdr[7]
	data = data_recv[20:]
	urg = bool(flags & 0x0020)
	ack = bool(flags & 0x0010)
	psh = bool(flags & 0x0008)
	rst = bool(flags & 0x0004)
	syn = bool(flags & 0x0002)
	fin = bool(flags & 0x0001)
	print("___________________________TCP HEADR_________________")
	print("Source : %hu " % src_port)
	print("Destination %hu " % dst_port)
	print("seq number %u " % seq_num)
	print("Ack %u " % ack_num)
	print("FLAG :")
	print("URG: %d " %urg)
	print("ack: %d " %ack)
	print("psh: %d " %psh)
	print("rst: %d " %rst)
	print("syn: %d " %syn)
	print("Fin: %d " %fin)
	return data


def analyze_ip_header(data_recv):
	ip_hdr = struct.unpack('!6H4s4s', data_recv[:20])
	ver = ip_hdr[0] >> 12
	ihl = (ip_hdr[0] >> 8) & 0x0f
	tos = ip_hdr[0] & 0x00ff
	tot_len = ip_hdr[1]
	ip_id = ip_hdr[2]
	flag = ip_hdr[3] >> 13
	frag_offset = ip_hdr[3] & 0x1fff
	ip_ttl = ip_hdr[4] >> 8
	ip_proto = ip_hdr[4] & 0x00ff
	checksum = ip_hdr[5]
	src_add = socket.inet_ntoa(ip_hdr[6])
	dst_address = socket.inet_ntoa(ip_hdr[7])
	data = data_recv[20:]
	print("------------------------IP Header---------------")
	print("version : %hu " %ver)
	print("IHL: %hu " % ihl)
	print("Tos : %hu " % tos)
	print("length : %hu " % tot_len)
	print("ID : %hu "% ip_id)
	print("Offset: %hu " % frag_offset)
	print("TTL: %hu " % ip_ttl)
	print("proto: %hu " % ip_proto)
	print("CheckSum: %hu " % checksum)
	print("source IP: %s" % src_add)
	print("Dest IP: %s " % dst_address)
	if ip_proto == 6:
		tcp_udp = "TCP"
	elif ip_proto == 17:
		tcp_udp = "UDP"
	else:
		tcp_udp = "OTHER"

	return data, tcp_udp




def analyze_ether_header(data_recv):
	ip_bool =  False
	eth_hdr = struct.unpack('!6s6sH', data_recv[:14])
	dest_mac = binascii.hexlify(eth_hdr[0])
	src_mac = binascii.hexlify(eth_hdr[1])
	proto = eth_hdr[2] >> 8
	data = data_recv[14:]
	print("----------------ETNERNET HEADER_________________")
	print("Destination MAC: %s:%s:%s:%s:%s:%s " % (dest_mac[0:2],dest_mac[2:4],dest_mac[4:6],dest_mac[6:8],dest_mac[8:10],src_mac[10:12]))
	print("Sorce  Mac: %s:%s:%s:%s:%s:%s" % (src_mac[0:2],src_mac[2:4],src_mac[4:6],src_mac[6:8],src_mac[8:10],src_mac[10:12]))
	print("Protocol: %hu" %proto)
	if proto == 0x08:
		ip_bool = True
	return data, ip_bool

def main():
	global socket_created
	global sniffer_socket
	if sock_created == False:
		sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,socket.htons(0x003))
		socket_created = True
	data_recv = sniffer_socket .recv(2048)
	os.system('clear')

	data_recv, ip_bool = analyze_ether_header(data_recv)
	if ip_bool:
		data_recv, tcp_udp = analyze_ip_header(data_recv)
	else:
		return

	if tcp_udp == "TCP":
		data_recv =  analyze_tcp_header(data_recv)
	elif tcp_udp == "UDP":
		data_recv = analyze_udp_header(data_recv)
	else:
		return

while True:
	main()



