def required_boxes(prod_count):
    box = prod_count/12
    round_box= round(box)
    if(round_box < box):
        round_box=+1
    return round_box
    