import os
import sys

methods_list = ['GradTTS_FS_S-I', 'GradTTS_MS_S-I', 'GradTTS_SS_S-I', 'MultiGradSpeech_FS_S-I', 'MultiGradSpeech_MS_S-I', 'MultiGradSpeech_MS_S-S', 'MultiGradSpeech_SS_S-I' , 'Recording', 'GradTTS_FS_S-S', 'GradTTS_MS_S-S', 'GradTTS_SS_S-S', 'MultiGradSpeech_FS_S-S', 'MultiGradSpeech_MS_S-I_wocdm', 'MultiGradSpeech_MS_S-S_wocdm', 'MultiGradSpeech_SS_S-S']

id_list = ['000563', '002670', '003296']

for i in range(len(methods_list)):
    for j in range(len(id_list)):
        source_path = f'/root/workspace/syn/icassp_2024_all/{methods_list[i]}/{id_list[j]}.wav'
        target_path = f'./{methods_list[i]}/{id_list[j]}.wav'
        os.system(f'cp -r  {source_path} {target_path}')

