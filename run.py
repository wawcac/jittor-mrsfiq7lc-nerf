import sys
import os
case=sys.argv[1]
if case=='Easyship':
    os.system('python jrender/demo7-nerf.py --config jrender/configs/Easyship.txt')
elif case=='Car':
    os.system('python JNeRF/tools/run_net.py --config-file JNeRF/projects/ngp/configs/ngp_comp-Car.py')
elif case=='Coffee':
    os.system('python JNeRF/tools/run_net.py --config-file JNeRF/projects/ngp/configs/ngp_comp-Coffee.py')
elif case=='Scar':
    os.system('python JNeRF/tools/run_net.py --config-file JNeRF/projects/ngp/configs/ngp_comp-Scar.py')
elif case=='Scarf':
    os.system('python JNeRF/tools/run_net.py --config-file JNeRF/projects/ngp/configs/ngp_comp-Scarf.py')
else:
    print('Error: Unknown case.')