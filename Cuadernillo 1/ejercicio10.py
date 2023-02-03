#TF = 9.0*TC/5.0 + 32.0
#grados_tf = 74
#grados_tc = (grados_tf - 32.0)*5.0/9.0
#print(f"Grados Centígrados: {grados_tf}")


def calculo (grados_tf: float ):
    grados_tc = (grados_tf - 32.0)*5.0/9.0
    print(f"Grados Centígrados: {grados_tc}")
    
#probador
calculo(10.5)
