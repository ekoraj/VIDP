import subprocess
import os
import logging

def verifier_fichier_entree(chemin_video):
    """
    Vérifie l'existence du fichier vidéo d'entrée.
    
    Args:
        chemin_video (str): Chemin complet du fichier vidéo
    
    Returns:
        bool: True si le fichier existe, False sinon
    """
    if not os.path.exists(chemin_video):
        logging.error(f"⚠️ Le fichier {chemin_video} n'existe pas.")
        return False
    return True

def downscale_video(video_entree, video_sortie, resolution):
    """
    Redimensionne une vidéo à la résolution spécifiée.
    
    Args:
        video_entree (str): Chemin de la vidéo source
        video_sortie (str): Chemin de la vidéo de destination
        resolution (int): Hauteur de la vidéo
    """
    parametres_ffmpeg = [
        "ffmpeg", "-i", video_entree, 
        "-vf", f"scale=-2:{resolution},setsar=1", 
        "-c:v", "libx264", 
        "-preset", "slow", 
        "-crf", "23", 
        video_sortie
    ]
    
    try:
        subprocess.run(parametres_ffmpeg, check=True)
        logging.info(f"✅ Vidéo downscalée en {resolution}p avec succès : {video_sortie}")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Erreur de downscaling : {e}")

def traiter_videos(input_video, output_360p, output_240p):
    """
    Processus principal de downscaling des vidéos.
    
    Args:
        input_video (str): Chemin de la vidéo source
        output_360p (str): Chemin de la vidéo de sortie 360p
        output_240p (str): Chemin de la vidéo de sortie 240p
    """
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    if verifier_fichier_entree(input_video):
        downscale_video(input_video, output_360p, 360)
        downscale_video(input_video, output_240p, 240)

def main():
    """Point d'entrée principal du script."""
    input_video = "/VIDP/input/input.mp4"
    output_360p = "/VIDP/data/output_360p.mp4"
    output_240p = "/VIDP/data/output_240p.mp4"
    
    traiter_videos(input_video, output_360p, output_240p)

if __name__ == "__main__":
    main()
