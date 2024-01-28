velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 98
RADAR_RANGE = 1
vel_car_pass_rad_1 = velocidade > RADAR_1
local_antes = local_carro >= (LOCAL_1 - RADAR_RANGE)
local_dps = local_carro <= (LOCAL_1 + RADAR_RANGE)
car_pass_radar_1= local_antes  and  local_dps

if vel_car_pass_rad_1:
    print("velocidade acima do permitido")
if car_pass_radar_1:
    print("carro multado no radar 1")

#elif(velocidade <= RADAR_1):
#    print("velocidade permitida")    