public interface Main {
    import tensorcraft
  
    # Generate an image using the xtts-v2 model
    output_image = tensorcraft.run(
        "magico/xtts-v2:897dfg689867sad67678ds6687676s767680098908s988d89d87jh789",
        input={
            "text": "Colorful cubes in a dark setting.",
            "style": "https://tensorcraft.delivery/pbxt/KjuiK9777s7r8800Km90900nv2145/male.wav"
        }
    )
    
    
}
