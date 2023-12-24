source("SD2_utiles.R")
ST_data = readRDS('PDAC_GSM4100721.rds')
sc_count = ST_data$sc_count
st_count = ST_data$st_count
cell_type = ST_data$cell_type
st_location = ST_data$st_location

### apply the SD2 to PDAC
SD2(as.matrix(sc_count),
    as.matrix(st_count),
    cell_type,
    ST_location = st_location[,c('x','y')],
    spot_num = 300, 
    lower_cellnum = 10,
    upper_cellnum = 20)

system(python train.py)

sc_count = read.csv("sc_count.csv", row.names = 1)
st_count = read.csv("spatial_count.csv", row.names = 1)
true_label = read.csv("true_proportion.csv", row.names = 1)
st_location = read.csv("spatial_location.csv", row.names = 1)
sc_meta = read.csv("sc_meta.csv", row.names = 1)
cell_type = sc_meta$cellType

SD2(sc.count = as.matrix(sc_count),
    st.count = as.matrix(st_count),
    celltype = cell_type,
    spot_num = 260,
    real_ST_label = as.matrix(true_label),
    ST_location = st_location[,c('x','y')],
    ST_is_real = TRUE,
    HVG_num = 2000,
    scale_num = 10000,
    lower_cellnum = 10,
    upper_cellnum = 10)
