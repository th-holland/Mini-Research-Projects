
solar_constant <- 1366 # W/m^2
albedo <- 0.3
sb_constant <- 5.67e-8 # W/m^2/K^4
emissivity <- 0.62
earth_radius <- 6371e3 # m

CtoK <- function(temp) {
    return(temp + 273.15)
}

KtoC <- function(temp) {
    return(temp - 273.15)
}

resultant_forcing <- function(temp) {
    input <- (solar_constant/4) * (1 - albedo)
    output <- emissivity * sb_constant * temp^4
    return(input - output)
}

delta_q <- function(temp, mass, specific_heat) {
    return(temp * mass * specific_heat)
}

delta_q_water <- function(temp, mass) {
    return(delta_q(temp, mass, 4180))
}

vol_sphere_diff <- function(r1, r2) {
    return((4/3) * pi * (r2^3 - r1^3))
}
# 1.1
print("1.1")
# and units J
print(paste(delta_q_water(1, vol_sphere_diff(earth_radius, earth_radius + 50e3)), "J"))

# 1.4

## function for T in terms of resultant forcing
temp_forcing <- function(delta_F) {
    return(((delta_F - (solar_constant/4) * (1 - albedo)) / (-emissivity * sb_constant))^(1/4))
}

print("1.4")
print(paste(temp_forcing(0), "K"))
print(paste(KtoC(temp_forcing(0)), "C"))

# 1.5

dT <- function(dt, effect_heat_cap, T_initial) {
    return((dt/effect_heat_cap) * (((solar_constant/4) * (1 - albedo)) - (emissivity * sb_constant * T_initial^4)))
}

print(dT(dt = 1, effect_heat_cap = 1, T_initial = 1))