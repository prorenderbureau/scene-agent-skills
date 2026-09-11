# Synthetic camera fixture

`landmarks.json` contains 24 original, deterministic 3D points and their known image projections. Twenty train the fit and four are held out. World units are metres; the test uses the explicitly documented camera convention. It is a numerical fixture, not a photographic reconstruction.

```sh
scene-agent camera-fit examples/camera/landmarks.json --out outputs/camera.json
scene-agent max-camera outputs/camera.json --out outputs/camera.ms
```

Ground truth: position `[0.3, -0.2, -8.0]`, world-to-camera rotation vector `[0.02, -0.03, 0.015]` radians, focal length 1050 pixels, image size 1200 × 900. The negative Z position is part of this abstract numerical setup, not a recommended architectural camera placement.

The test also shifts one held-out image point by 80 pixels. Training error stays small while holdout RMS exceeds 39 pixels, demonstrating why independent points matter. Native camera transfer is checked by projecting these same points through Max's camera transform.
