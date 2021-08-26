# state file generated using paraview version 5.8.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

filename = 'everest__Multiview_' + str(sys.argv[1]).zfill(4) + '.png'
dt = int(sys.argv[1])
n_streams = 300

#image resolution
res_x = int(sys.argv[2])
res_y = int(sys.argv[3])


# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [712, 376]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0038862526416778564, 0.0, -0.004494160413742065]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.03173513972108392, -0.380329863505669, -0.03874664533838831]
renderView1.CameraFocalPoint = [-0.03173513972108392, 0.0, -0.03874664533838831]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.08166297494027437
renderView1.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView1.Background2 = [0.0, 0.0, 0.0]
renderView1.EnableRayTracing = 1
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.AmbientSamples = 1
renderView1.SamplesPerPixel = 16
renderView1.Denoise = 0
renderView1.TemporalCacheSize = 4
renderView1.BackgroundNorth = [1.0, 0.0, 0.0]
renderView1.BackgroundEast = [0.0, 1.0, 0.0]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [711, 363]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0038862526416778564, 0.0, -0.004494160413742065]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-0.03285548831840105, -0.6737775533219668, -0.03789429521771125]
renderView2.CameraFocalPoint = [-0.03285548831840105, 0.0, -0.03789429521771125]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 0.08065613493356827
renderView2.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView2.EnableRayTracing = 1
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.AmbientSamples = 1
renderView2.SamplesPerPixel = 16
renderView2.Denoise = 0
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [300, 376]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.04728114977478981, 0.0, -0.004494160413742065]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [-0.5067509234783554, -0.0004630845961597547, -0.02799105845096824]
renderView3.CameraFocalPoint = [0.04728114977478981, -0.0004630845961597547, -0.02799105845096824]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 0.08025393419951785
renderView3.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView3.EnableRayTracing = 1
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.AmbientSamples = 1
renderView3.SamplesPerPixel = 16
renderView3.Denoise = 0
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [431, 376]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.04728114977478981, 0.0, -0.004494160413742065]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [0.0026834702650966, 0.0006002706179606531, 0.18161212738187246]
renderView4.CameraFocalPoint = [0.0026834702650966, 0.0006002706179606531, -0.03199122058960833]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 0.04568976409312404
renderView4.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView4.EnableRayTracing = 1
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.AmbientSamples = 1
renderView4.SamplesPerPixel = 16
renderView4.Denoise = 0
renderView4.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [303, 363]
renderView5.InteractionMode = '2D'
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [0.04753166437149048, 5.289912223815918e-07, -0.004494160413742065]
renderView5.StereoType = 'Crystal Eyes'
renderView5.CameraPosition = [-0.505290897268397, -0.0017224683128397728, -0.033102417537792916]
renderView5.CameraFocalPoint = [0.04753166437149048, -0.0017224683128397728, -0.033102417537792916]
renderView5.CameraViewUp = [0.0, 0.0, 1.0]
renderView5.CameraFocalDisk = 1.0
renderView5.CameraParallelScale = 0.08076549862791348
renderView5.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView5.EnableRayTracing = 1
renderView5.BackEnd = 'OSPRay raycaster'
renderView5.AmbientSamples = 1
renderView5.SamplesPerPixel = 16
renderView5.Denoise = 0
renderView5.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView6 = CreateView('RenderView')
renderView6.ViewSize = [429, 363]
renderView6.InteractionMode = '2D'
renderView6.AxesGrid = 'GridAxes3DActor'
renderView6.OrientationAxesVisibility = 0
renderView6.CenterOfRotation = [0.04753166437149048, 5.289912223815918e-07, -0.004494160413742065]
renderView6.StereoType = 'Crystal Eyes'
renderView6.CameraPosition = [0.0015842202038009194, 3.5313044948287204e-05, 0.20864286847176003]
renderView6.CameraFocalPoint = [0.0015842202038009194, 3.5313044948287204e-05, -0.004494160413742065]
renderView6.CameraFocalDisk = 1.0
renderView6.CameraParallelScale = 0.04559001842325126
renderView6.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView6.EnableRayTracing = 1
renderView6.BackEnd = 'OSPRay raycaster'
renderView6.AmbientSamples = 1
renderView6.SamplesPerPixel = 16
renderView6.Denoise = 0
renderView6.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.507229)
layout1.SplitHorizontal(1, 0.489493)
layout1.AssignView(3, renderView1)
layout1.SplitHorizontal(4, 0.410693)
layout1.AssignView(9, renderView3)
layout1.AssignView(10, renderView4)
layout1.SplitHorizontal(2, 0.488875)
layout1.AssignView(5, renderView2)
layout1.SplitHorizontal(6, 0.415049)
layout1.AssignView(13, renderView5)
layout1.AssignView(14, renderView6)

#Added by hand
layout1.SetSize(res_x, res_y)


# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView4)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Text'
high = Text()
high.Text = 'High'

# create a new 'PVD Reader'
pvpvd = PVDReader(FileName='/gpfs/alpine/proj-shared/cmb124/paraview_files/gEqnPlusKinetics_b1_14_b3_6_LES_map_b1_16_cycle2/pv.pvd')
pvpvd.CellArrays = ['G_EQN_TRANSPORT', 'TEMPERATURE', 'velocity']

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(Input=pvpvd)
extractTimeSteps1.TimeStepIndices = [87]
extractTimeSteps1.TimeStepRange = [0, 503]

# create a new 'Extract Block'
parcel = ExtractBlock(Input=extractTimeSteps1)
parcel.BlockIndices = [2]

# create a new 'Extract Block'
intakeExhaust_Geometry = ExtractBlock(Input=extractTimeSteps1)
intakeExhaust_Geometry.BlockIndices = [7, 6, 23, 5, 22, 21, 3, 20, 19, 17, 15, 16, 14, 13, 12, 8]
intakeExhaust_Geometry.MaintainStructure = 1

# create a new 'Extract Block'
head = ExtractBlock(Input=intakeExhaust_Geometry)
head.BlockIndices = [2]

# create a new 'Extract Block'
intake_Geometry = ExtractBlock(Input=intakeExhaust_Geometry)
intake_Geometry.BlockIndices = [8, 7, 6, 5, 4, 3, 1, 10, 9]

# create a new 'Extract Block'
plug = ExtractBlock(Input=intake_Geometry)
plug.BlockIndices = [3, 2]

# create a new 'Text'
low = Text()
low.Text = 'Low'

# create a new 'Threshold'
threshold1 = Threshold(Input=parcel)
threshold1.Scalars = ['POINTS', 'dp_TEMP']
threshold1.ThresholdRange = [0.0, 390.0]

# create a new 'Extract Block'
cell = ExtractBlock(Input=extractTimeSteps1)
cell.BlockIndices = [1]

# create a new 'Stream Tracer'
intake_FrontStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
intake_FrontStreamTracer.Vectors = ['CELLS', 'velocity']
intake_FrontStreamTracer.MinimumStepLength = 0.09
intake_FrontStreamTracer.MaximumStepLength = 0.2
intake_FrontStreamTracer.MaximumStreamlineLength = 4.0
intake_FrontStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
intake_FrontStreamTracer.SeedType.Center = [0.021382743796776224, -0.01875330655923476, 0.019222949852495272]
intake_FrontStreamTracer.SeedType.NumberOfPoints = n_streams
intake_FrontStreamTracer.SeedType.Radius = 0.022

# create a new 'Glyph'
intake_FrontArrows = Glyph(Input=intake_FrontStreamTracer,
    GlyphType='Arrow')
intake_FrontArrows.OrientationArray = ['POINTS', 'velocity']
intake_FrontArrows.ScaleArray = ['POINTS', 'No scale array']
intake_FrontArrows.ScaleFactor = 0.005
intake_FrontArrows.GlyphTransform = 'Transform2'
intake_FrontArrows.GlyphMode = 'Every Nth Point'
intake_FrontArrows.MaximumNumberOfSamplePoints = 9000
intake_FrontArrows.Seed = 5000
intake_FrontArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
intake_FrontArrows.GlyphType.TipRadius = 0.2

# create a new 'Stream Tracer'
exhaust_FrontStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
exhaust_FrontStreamTracer.Vectors = ['CELLS', 'velocity']
exhaust_FrontStreamTracer.MinimumStepLength = 0.09
exhaust_FrontStreamTracer.MaximumStepLength = 0.2
exhaust_FrontStreamTracer.MaximumStreamlineLength = 4.0
exhaust_FrontStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
exhaust_FrontStreamTracer.SeedType.Center = [-0.0213827, -0.0187533, 0.0192229]
exhaust_FrontStreamTracer.SeedType.NumberOfPoints = n_streams
exhaust_FrontStreamTracer.SeedType.Radius = 0.02

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(Input=cell)
pythonAnnotation1.Expression = '"CA %3.3f" % Crank_Angle[0]'

# create a new 'Stream Tracer'
intake_BackStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
intake_BackStreamTracer.Vectors = ['CELLS', 'velocity']
intake_BackStreamTracer.MinimumStepLength = 0.09
intake_BackStreamTracer.MaximumStepLength = 0.2
intake_BackStreamTracer.MaximumStreamlineLength = 4.0
intake_BackStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
intake_BackStreamTracer.SeedType.Center = [0.0213827, 0.0187533, 0.0192229]
intake_BackStreamTracer.SeedType.NumberOfPoints = n_streams
intake_BackStreamTracer.SeedType.Radius = 0.022

# create a new 'Stream Tracer'
exhaust_BackStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
exhaust_BackStreamTracer.Vectors = ['CELLS', 'velocity']
exhaust_BackStreamTracer.MinimumStepLength = 0.09
exhaust_BackStreamTracer.MaximumStepLength = 0.2
exhaust_BackStreamTracer.MaximumStreamlineLength = 4.0
exhaust_BackStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
exhaust_BackStreamTracer.SeedType.Center = [-0.0213827, 0.0187533, 0.0192229]
exhaust_BackStreamTracer.SeedType.NumberOfPoints = n_streams
exhaust_BackStreamTracer.SeedType.Radius = 0.02

# create a new 'Cell Data to Point Data'
cell2Point_EQN_TRANS = CellDatatoPointData(Input=cell)
cell2Point_EQN_TRANS.ProcessAllArrays = 0
cell2Point_EQN_TRANS.CellDataArraytoprocess = ['G_EQN_TRANSPORT']

# create a new 'Contour'
contour1 = Contour(Input=cell2Point_EQN_TRANS)
contour1.ContourBy = ['POINTS', 'G_EQN_TRANSPORT']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Glyph'
intake_BackArrows = Glyph(Input=intake_BackStreamTracer,
    GlyphType='Arrow')
intake_BackArrows.OrientationArray = ['POINTS', 'velocity']
intake_BackArrows.ScaleArray = ['POINTS', 'No scale array']
intake_BackArrows.ScaleFactor = 0.005
intake_BackArrows.GlyphTransform = 'Transform2'
intake_BackArrows.GlyphMode = 'Every Nth Point'
intake_BackArrows.MaximumNumberOfSamplePoints = 9000
intake_BackArrows.Seed = 5000
intake_BackArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
intake_BackArrows.GlyphType.TipRadius = 0.2

# create a new 'Glyph'
exhaust_BackArrows = Glyph(Input=exhaust_BackStreamTracer,
    GlyphType='Arrow')
exhaust_BackArrows.OrientationArray = ['POINTS', 'velocity']
exhaust_BackArrows.ScaleArray = ['POINTS', 'No scale array']
exhaust_BackArrows.ScaleFactor = 0.005
exhaust_BackArrows.GlyphTransform = 'Transform2'
exhaust_BackArrows.GlyphMode = 'Every Nth Point'
exhaust_BackArrows.MaximumNumberOfSamplePoints = 9000
exhaust_BackArrows.Seed = 5000
exhaust_BackArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
exhaust_BackArrows.GlyphType.TipRadius = 0.2

# create a new 'Glyph'
exhaust_FrontArrows = Glyph(Input=exhaust_FrontStreamTracer,
    GlyphType='Arrow')
exhaust_FrontArrows.OrientationArray = ['POINTS', 'velocity']
exhaust_FrontArrows.ScaleArray = ['POINTS', 'No scale array']
exhaust_FrontArrows.ScaleFactor = 0.005
exhaust_FrontArrows.GlyphTransform = 'Transform2'
exhaust_FrontArrows.GlyphMode = 'Every Nth Point'
exhaust_FrontArrows.MaximumNumberOfSamplePoints = 9000
exhaust_FrontArrows.Seed = 5000
exhaust_FrontArrows.Stride = 100

# init the 'Arrow' selected for 'GlyphType'
exhaust_FrontArrows.GlyphType.TipRadius = 0.2

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from intakeExhaust_Geometry
intakeExhaust_GeometryDisplay = Show(intakeExhaust_Geometry, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intakeExhaust_GeometryDisplay.Representation = 'Surface'
intakeExhaust_GeometryDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay.ColorArrayName = ['POINTS', '']
intakeExhaust_GeometryDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay.Opacity = 0.25
intakeExhaust_GeometryDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay.SelectOrientationVectors = 'None'
intakeExhaust_GeometryDisplay.ScaleFactor = 0.010390702914446593
intakeExhaust_GeometryDisplay.SelectScaleArray = 'None'
intakeExhaust_GeometryDisplay.GlyphType = 'Arrow'
intakeExhaust_GeometryDisplay.GlyphTableIndexArray = 'None'
intakeExhaust_GeometryDisplay.GaussianRadius = 0.0005195351457223296
intakeExhaust_GeometryDisplay.SetScaleArray = [None, '']
intakeExhaust_GeometryDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay.OpacityArray = [None, '']
intakeExhaust_GeometryDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay.DataAxesGrid = 'GridAxesRepresentation'
intakeExhaust_GeometryDisplay.PolarAxes = 'PolarAxesRepresentation'
intakeExhaust_GeometryDisplay.ScalarOpacityUnitDistance = 0.001630907728715554
intakeExhaust_GeometryDisplay.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay = Show(intake_FrontStreamTracer, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.AutomaticRescaleRangeMode = 'Never'
velocityLUT.RGBPoints = [12.138645935859405, 0.278431372549, 0.278431372549, 0.858823529412, 49.072270818764466, 0.0, 0.0, 0.360784313725, 85.74761860458625, 0.0, 1.0, 1.0, 122.9395205845746, 0.0, 0.501960784314, 0.0, 159.61486837039638, 1.0, 1.0, 0.0, 196.54849325330144, 1.0, 0.380392156863, 0.0, 233.4821181362065, 0.419607843137, 0.0, 0.0, 270.4157430191116, 0.878431372549, 0.301960784314, 0.301960784314]
velocityLUT.ColorSpace = 'RGB'
velocityLUT.Discretize = 0
velocityLUT.NumberOfTableValues = 6
velocityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay.Representation = 'Wireframe'
intake_FrontStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay.LineWidth = 0.3
intake_FrontStreamTracerDisplay.OSPRayScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay.SelectOrientationVectors = 'Normals'
intake_FrontStreamTracerDisplay.ScaleFactor = 0.01835412085056305
intake_FrontStreamTracerDisplay.SelectScaleArray = 'AngularVelocity'
intake_FrontStreamTracerDisplay.GlyphType = 'Arrow'
intake_FrontStreamTracerDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_FrontStreamTracerDisplay.GaussianRadius = 0.0009177060425281525
intake_FrontStreamTracerDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_FrontStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_FrontStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontStreamTracerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontStreamTracerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from intake_BackStreamTracer
intake_BackStreamTracerDisplay = Show(intake_BackStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackStreamTracerDisplay.Representation = 'Wireframe'
intake_BackStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
intake_BackStreamTracerDisplay.LookupTable = velocityLUT
intake_BackStreamTracerDisplay.LineWidth = 0.3
intake_BackStreamTracerDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_BackStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay.SelectOrientationVectors = 'Normals'
intake_BackStreamTracerDisplay.ScaleFactor = 0.003236056445166469
intake_BackStreamTracerDisplay.SelectScaleArray = 'AngularVelocity'
intake_BackStreamTracerDisplay.GlyphType = 'Arrow'
intake_BackStreamTracerDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_BackStreamTracerDisplay.GaussianRadius = 0.00016180282225832342
intake_BackStreamTracerDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_BackStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_BackStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_BackStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackStreamTracerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackStreamTracerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from exhaust_FrontStreamTracer
exhaust_FrontStreamTracerDisplay = Show(exhaust_FrontStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontStreamTracerDisplay.Representation = 'Wireframe'
exhaust_FrontStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
exhaust_FrontStreamTracerDisplay.LookupTable = velocityLUT
exhaust_FrontStreamTracerDisplay.LineWidth = 0.3
exhaust_FrontStreamTracerDisplay.OSPRayScaleArray = 'AngularVelocity'
exhaust_FrontStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay.SelectOrientationVectors = 'Normals'
exhaust_FrontStreamTracerDisplay.ScaleFactor = 0.00614069551229477
exhaust_FrontStreamTracerDisplay.SelectScaleArray = 'AngularVelocity'
exhaust_FrontStreamTracerDisplay.GlyphType = 'Arrow'
exhaust_FrontStreamTracerDisplay.GlyphTableIndexArray = 'AngularVelocity'
exhaust_FrontStreamTracerDisplay.GaussianRadius = 0.0003070347756147385
exhaust_FrontStreamTracerDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
exhaust_FrontStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
exhaust_FrontStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontStreamTracerDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontStreamTracerDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay = Show(exhaust_BackStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay.Representation = 'Wireframe'
exhaust_BackStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay.LineWidth = 0.3
exhaust_BackStreamTracerDisplay.OSPRayScaleArray = 'velocity'
exhaust_BackStreamTracerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.ScaleFactor = 0.00973363183438778
exhaust_BackStreamTracerDisplay.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay.GaussianRadius = 0.00048668159171938897
exhaust_BackStreamTracerDisplay.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay.ScaleTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay.OpacityTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from intake_Geometry
intake_GeometryDisplay = Show(intake_Geometry, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay.Representation = 'Surface'
intake_GeometryDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay.ColorArrayName = ['POINTS', '']
intake_GeometryDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay.Opacity = 0.25
intake_GeometryDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay.SelectOrientationVectors = 'None'
intake_GeometryDisplay.ScaleFactor = 0.027035209536552432
intake_GeometryDisplay.SelectScaleArray = 'None'
intake_GeometryDisplay.GlyphType = 'Arrow'
intake_GeometryDisplay.GlyphTableIndexArray = 'None'
intake_GeometryDisplay.GaussianRadius = 0.0013517604768276215
intake_GeometryDisplay.SetScaleArray = [None, '']
intake_GeometryDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay.OpacityArray = [None, '']
intake_GeometryDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay.ScalarOpacityUnitDistance = 0.0023014537338361435
intake_GeometryDisplay.ExtractedBlockIndex = 1

# show data from plug
plugDisplay = Show(plug, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay.Representation = 'Surface'
plugDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay.ColorArrayName = ['POINTS', '']
plugDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay.Opacity = 0.7
plugDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay.SelectOrientationVectors = 'None'
plugDisplay.ScaleFactor = 0.020157745480537417
plugDisplay.SelectScaleArray = 'None'
plugDisplay.GlyphType = 'Arrow'
plugDisplay.GlyphTableIndexArray = 'None'
plugDisplay.GaussianRadius = 0.0010078872740268707
plugDisplay.SetScaleArray = [None, '']
plugDisplay.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay.OpacityArray = [None, '']
plugDisplay.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay.PolarAxes = 'PolarAxesRepresentation'
plugDisplay.ScalarOpacityUnitDistance = 0.002310755212500419
plugDisplay.ExtractedBlockIndex = 1

# show data from low
lowDisplay = Show(low, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
lowDisplay.Color = [0.0, 0.0, 0.0]
lowDisplay.FontSize = 15
lowDisplay.WindowLocation = 'AnyLocation'
lowDisplay.Position = [0.09, 0.0]

# show data from high
highDisplay = Show(high, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
highDisplay.Color = [0.0, 0.0, 0.0]
highDisplay.FontSize = 15
highDisplay.WindowLocation = 'AnyLocation'
highDisplay.Position = [0.09, 0.47]

# setup the color legend parameters for each legend in this view

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.AutoOrient = 0
velocityLUTColorBar.WindowLocation = 'LowerLeftCorner'
velocityLUTColorBar.Position = [0.03881278538812785, 0.010638297872340425]
velocityLUTColorBar.Title = 'VELOCITY'
velocityLUTColorBar.ComponentTitle = ''
velocityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.TitleFontSize = 20
velocityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.LabelFontSize = 18
velocityLUTColorBar.AutomaticLabelFormat = 0
velocityLUTColorBar.DrawTickMarks = 0
velocityLUTColorBar.DrawTickLabels = 0
velocityLUTColorBar.CustomLabels = [0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 0.0]
velocityLUTColorBar.AddRangeLabels = 0
velocityLUTColorBar.DrawAnnotations = 0
velocityLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
velocityLUTColorBar.ScalarBarThickness = 14
velocityLUTColorBar.ScalarBarLength = 0.5000000000000001

# set color bar visibility
velocityLUTColorBar.Visibility = 1

# show color legend
intake_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
intake_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
exhaust_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
exhaust_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_1 = Show(intake_Geometry, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_1.Representation = 'Surface'
intake_GeometryDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_1.ColorArrayName = [None, '']
intake_GeometryDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_1.Opacity = 0.25
intake_GeometryDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_1.SelectOrientationVectors = 'None'
intake_GeometryDisplay_1.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_1.SelectScaleArray = 'None'
intake_GeometryDisplay_1.GlyphType = 'Arrow'
intake_GeometryDisplay_1.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_1.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_1.SetScaleArray = [None, '']
intake_GeometryDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_1.OpacityArray = [None, '']
intake_GeometryDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_1.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_1.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_1.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_1 = Show(plug, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_1.Representation = 'Surface'
plugDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_1.ColorArrayName = [None, '']
plugDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_1.Opacity = 0.7
plugDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_1.SelectOrientationVectors = 'None'
plugDisplay_1.ScaleFactor = 0.00010781330056488515
plugDisplay_1.SelectScaleArray = 'None'
plugDisplay_1.GlyphType = 'Arrow'
plugDisplay_1.GlyphTableIndexArray = 'None'
plugDisplay_1.GaussianRadius = 5.390665028244257e-06
plugDisplay_1.SetScaleArray = [None, '']
plugDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_1.OpacityArray = [None, '']
plugDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_1.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_1.ScalarOpacityUnitDistance = 0.00016043032651082378
plugDisplay_1.ExtractedBlockIndex = 1

# show data from intakeExhaust_Geometry
intakeExhaust_GeometryDisplay_1 = Show(intakeExhaust_Geometry, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intakeExhaust_GeometryDisplay_1.Representation = 'Surface'
intakeExhaust_GeometryDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay_1.ColorArrayName = ['POINTS', '']
intakeExhaust_GeometryDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intakeExhaust_GeometryDisplay_1.Opacity = 0.25
intakeExhaust_GeometryDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_1.SelectOrientationVectors = 'None'
intakeExhaust_GeometryDisplay_1.ScaleFactor = 0.027035209536552432
intakeExhaust_GeometryDisplay_1.SelectScaleArray = 'None'
intakeExhaust_GeometryDisplay_1.GlyphType = 'Arrow'
intakeExhaust_GeometryDisplay_1.GlyphTableIndexArray = 'None'
intakeExhaust_GeometryDisplay_1.GaussianRadius = 0.0013517604768276215
intakeExhaust_GeometryDisplay_1.SetScaleArray = [None, '']
intakeExhaust_GeometryDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_1.OpacityArray = [None, '']
intakeExhaust_GeometryDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intakeExhaust_GeometryDisplay_1.PolarAxes = 'PolarAxesRepresentation'
intakeExhaust_GeometryDisplay_1.ScalarOpacityUnitDistance = 0.0023014537338361435
intakeExhaust_GeometryDisplay_1.ExtractedBlockIndex = 1

# show data from contour1
contour1Display = Show(contour1, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUT = GetColorTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTLUT.RGBPoints = [-0.10000014305114746, 0.0, 0.0, 0.5625, -0.08888902715659142, 0.0, 0.0, 1.0, -0.06349214082610607, 0.0, 1.0, 1.0, -0.05079372266089916, 0.5, 1.0, 0.5, -0.038095304495692255, 1.0, 1.0, 0.0, -0.012698418165206907, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0]
g_EQN_TRANSPORTLUT.ColorSpace = 'RGB'
g_EQN_TRANSPORTLUT.NanColor = [0.0, 1.0, 0.0]
g_EQN_TRANSPORTLUT.Discretize = 0
g_EQN_TRANSPORTLUT.NumberOfTableValues = 1
g_EQN_TRANSPORTLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.LookupTable = g_EQN_TRANSPORTLUT
contour1Display.Specular = 1.0
contour1Display.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display.SpecularPower = 10.0
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = -2.0000000000000002e+298
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.GaussianRadius = -1e+297
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# show data from threshold1
threshold1Display = Show(threshold1, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'dp_FROM_NOZZLE'
dp_FROM_NOZZLELUT = GetColorTransferFunction('dp_FROM_NOZZLE')
dp_FROM_NOZZLELUT.InterpretValuesAsCategories = 1
dp_FROM_NOZZLELUT.AnnotationsInitialized = 1
dp_FROM_NOZZLELUT.EnableOpacityMapping = 1
dp_FROM_NOZZLELUT.RGBPoints = [0.0, 0.4745098039215686, 0.09019607843137255, 0.09019607843137255, 0.0, 1.0, 0.3333333333333333, 0.0, 1.0, 1.0, 0.3333333333333333, 0.0]
dp_FROM_NOZZLELUT.ColorSpace = 'Step'
dp_FROM_NOZZLELUT.NanColor = [1.0, 0.8980392156862745, 0.02352941176470588]
dp_FROM_NOZZLELUT.NumberOfTableValues = 2
dp_FROM_NOZZLELUT.ScalarRangeInitialized = 1.0
dp_FROM_NOZZLELUT.Annotations = ['0', '0', '1', '1']
dp_FROM_NOZZLELUT.ActiveAnnotatedValues = ['0', '1', '0', '1']
dp_FROM_NOZZLELUT.IndexedColors = [1.0, 0.3333333333333333, 0.0, 0.7098039215686275, 0.23529411764705882, 0.0]
dp_FROM_NOZZLELUT.IndexedOpacities = [1.0, 1.0]

# get opacity transfer function/opacity map for 'dp_FROM_NOZZLE'
dp_FROM_NOZZLEPWF = GetOpacityTransferFunction('dp_FROM_NOZZLE')
dp_FROM_NOZZLEPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
dp_FROM_NOZZLEPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.AmbientColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display.ColorArrayName = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display.DiffuseColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display.LookupTable = dp_FROM_NOZZLELUT
threshold1Display.OSPRayScaleArray = 'dp_FROM_NOZZLE'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 0.008697206526994706
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = 0.0004348603263497353
threshold1Display.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = dp_FROM_NOZZLEPWF
threshold1Display.ScalarOpacityUnitDistance = 0.0050929497409951735
threshold1Display.ExtractedBlockIndex = 1

# show data from pythonAnnotation1
pythonAnnotation1Display = Show(pythonAnnotation1, renderView2, 'TextSourceRepresentation')

# trace defaults for the display properties.
pythonAnnotation1Display.Color = [0.0, 0.0, 0.0]
pythonAnnotation1Display.WindowLocation = 'AnyLocation'
pythonAnnotation1Display.Position = [0.02, 0.87]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_2 = Show(intake_Geometry, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_2.Representation = 'Surface'
intake_GeometryDisplay_2.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_2.ColorArrayName = [None, '']
intake_GeometryDisplay_2.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_2.Opacity = 0.25
intake_GeometryDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_2.SelectOrientationVectors = 'None'
intake_GeometryDisplay_2.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_2.SelectScaleArray = 'None'
intake_GeometryDisplay_2.GlyphType = 'Arrow'
intake_GeometryDisplay_2.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_2.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_2.SetScaleArray = [None, '']
intake_GeometryDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_2.OpacityArray = [None, '']
intake_GeometryDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_2.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_2.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_2.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_2 = Show(plug, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_2.Representation = 'Surface'
plugDisplay_2.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_2.ColorArrayName = [None, '']
plugDisplay_2.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_2.Opacity = 0.7
plugDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_2.SelectOrientationVectors = 'None'
plugDisplay_2.ScaleFactor = 0.0010427969042211772
plugDisplay_2.SelectScaleArray = 'None'
plugDisplay_2.GlyphType = 'Arrow'
plugDisplay_2.GlyphTableIndexArray = 'None'
plugDisplay_2.GaussianRadius = 5.2139845211058853e-05
plugDisplay_2.SetScaleArray = [None, '']
plugDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_2.OpacityArray = [None, '']
plugDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_2.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_2.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_2.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay_1 = Show(intake_FrontStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay_1.Representation = 'Wireframe'
intake_FrontStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay_1.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay_1.LineWidth = 0.3
intake_FrontStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.ScaleFactor = 0.014265598356723787
intake_FrontStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.GlyphType = 'Arrow'
intake_FrontStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_1.GaussianRadius = 0.0007132799178361893
intake_FrontStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# show data from intake_BackStreamTracer
intake_BackStreamTracerDisplay_1 = Show(intake_BackStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackStreamTracerDisplay_1.Representation = 'Wireframe'
intake_BackStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
intake_BackStreamTracerDisplay_1.LookupTable = velocityLUT
intake_BackStreamTracerDisplay_1.LineWidth = 0.3
intake_BackStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.ScaleFactor = 0.014364903420209886
intake_BackStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.GlyphType = 'Arrow'
intake_BackStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_1.GaussianRadius = 0.0007182451710104942
intake_BackStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_BackStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# show data from exhaust_FrontStreamTracer
exhaust_FrontStreamTracerDisplay_1 = Show(exhaust_FrontStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontStreamTracerDisplay_1.Representation = 'Wireframe'
exhaust_FrontStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
exhaust_FrontStreamTracerDisplay_1.LookupTable = velocityLUT
exhaust_FrontStreamTracerDisplay_1.LineWidth = 0.3
exhaust_FrontStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.ScaleFactor = 0.014060626551508904
exhaust_FrontStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.GlyphType = 'Arrow'
exhaust_FrontStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_1.GaussianRadius = 0.0007030313275754452
exhaust_FrontStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay_1 = Show(exhaust_BackStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay_1.Representation = 'Wireframe'
exhaust_BackStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay_1.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay_1.LineWidth = 0.3
exhaust_BackStreamTracerDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.ScaleFactor = 0.014190616831183434
exhaust_BackStreamTracerDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_1.GaussianRadius = 0.0007095308415591717
exhaust_BackStreamTracerDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay_1.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay_1.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# show data from head
headDisplay = Show(head, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay.Representation = 'Surface'
headDisplay.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay.ColorArrayName = [None, '']
headDisplay.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay.Opacity = 0.25
headDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
headDisplay.SelectOrientationVectors = 'None'
headDisplay.ScaleFactor = 0.008899322897195817
headDisplay.SelectScaleArray = 'None'
headDisplay.GlyphType = 'Arrow'
headDisplay.GlyphTableIndexArray = 'None'
headDisplay.GaussianRadius = 0.0004449661448597908
headDisplay.SetScaleArray = [None, '']
headDisplay.ScaleTransferFunction = 'PiecewiseFunction'
headDisplay.OpacityArray = [None, '']
headDisplay.OpacityTransferFunction = 'PiecewiseFunction'
headDisplay.DataAxesGrid = 'GridAxesRepresentation'
headDisplay.PolarAxes = 'PolarAxesRepresentation'
headDisplay.ScalarOpacityUnitDistance = 0.0016640944230168922
headDisplay.ExtractedBlockIndex = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_3 = Show(intake_Geometry, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_3.Representation = 'Surface'
intake_GeometryDisplay_3.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_3.ColorArrayName = [None, '']
intake_GeometryDisplay_3.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_3.Opacity = 0.25
intake_GeometryDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_3.SelectOrientationVectors = 'None'
intake_GeometryDisplay_3.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_3.SelectScaleArray = 'None'
intake_GeometryDisplay_3.GlyphType = 'Arrow'
intake_GeometryDisplay_3.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_3.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_3.SetScaleArray = [None, '']
intake_GeometryDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_3.OpacityArray = [None, '']
intake_GeometryDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_3.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_3.ScalarOpacityUnitDistance = 0.0021597388225030813
intake_GeometryDisplay_3.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_3 = Show(plug, renderView4, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_3.Representation = 'Surface'
plugDisplay_3.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_3.ColorArrayName = [None, '']
plugDisplay_3.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_3.Opacity = 0.7
plugDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_3.SelectOrientationVectors = 'None'
plugDisplay_3.ScaleFactor = 0.0010427969042211772
plugDisplay_3.SelectScaleArray = 'None'
plugDisplay_3.GlyphType = 'Arrow'
plugDisplay_3.GlyphTableIndexArray = 'None'
plugDisplay_3.GaussianRadius = 5.2139845211058853e-05
plugDisplay_3.SetScaleArray = [None, '']
plugDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_3.OpacityArray = [None, '']
plugDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_3.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_3.ScalarOpacityUnitDistance = 0.0004946801360981299
plugDisplay_3.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay_2 = Show(intake_FrontStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay_2.Representation = 'Wireframe'
intake_FrontStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay_2.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay_2.LineWidth = 0.3
intake_FrontStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.ScaleFactor = 0.014265598356723787
intake_FrontStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.GlyphType = 'Arrow'
intake_FrontStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontStreamTracerDisplay_2.GaussianRadius = 0.0007132799178361893
intake_FrontStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.0042878329116381965, 0.0, 0.5, 0.0, 0.014851102825360389, 1.0, 0.5, 0.0]

# show data from intake_BackStreamTracer
intake_BackStreamTracerDisplay_2 = Show(intake_BackStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackStreamTracerDisplay_2.Representation = 'Wireframe'
intake_BackStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
intake_BackStreamTracerDisplay_2.LookupTable = velocityLUT
intake_BackStreamTracerDisplay_2.LineWidth = 0.3
intake_BackStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.ScaleFactor = 0.014364903420209886
intake_BackStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.GlyphType = 'Arrow'
intake_BackStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_BackStreamTracerDisplay_2.GaussianRadius = 0.0007182451710104942
intake_BackStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_BackStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.0065038254316704775, 0.0, 0.5, 0.0, 0.04722794023529797, 1.0, 0.5, 0.0]

# show data from exhaust_FrontStreamTracer
exhaust_FrontStreamTracerDisplay_2 = Show(exhaust_FrontStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontStreamTracerDisplay_2.Representation = 'Wireframe'
exhaust_FrontStreamTracerDisplay_2.AmbientColor = [0.0, 0.0, 0.0]
exhaust_FrontStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
exhaust_FrontStreamTracerDisplay_2.DiffuseColor = [0.0, 0.0, 0.0]
exhaust_FrontStreamTracerDisplay_2.LookupTable = velocityLUT
exhaust_FrontStreamTracerDisplay_2.InterpolateScalarsBeforeMapping = 0
exhaust_FrontStreamTracerDisplay_2.LineWidth = 0.5
exhaust_FrontStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.ScaleFactor = 0.014060626551508904
exhaust_FrontStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.GlyphType = 'Arrow'
exhaust_FrontStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontStreamTracerDisplay_2.GaussianRadius = 0.0007030313275754452
exhaust_FrontStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.007387990865260271, 0.0, 0.5, 0.0, 0.11506846833487049, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay_2 = Show(exhaust_BackStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay_2.Representation = 'Wireframe'
exhaust_BackStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay_2.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay_2.LineWidth = 0.5
exhaust_BackStreamTracerDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.ScaleFactor = 0.014190616831183434
exhaust_BackStreamTracerDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_2.GaussianRadius = 0.0007095308415591717
exhaust_BackStreamTracerDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay_2.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay_2.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.009544930566093174, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_4 = Show(intake_Geometry, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_4.Representation = 'Surface'
intake_GeometryDisplay_4.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_4.ColorArrayName = [None, '']
intake_GeometryDisplay_4.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_4.Opacity = 0.25
intake_GeometryDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_4.SelectOrientationVectors = 'None'
intake_GeometryDisplay_4.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_4.SelectScaleArray = 'None'
intake_GeometryDisplay_4.GlyphType = 'Arrow'
intake_GeometryDisplay_4.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_4.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_4.SetScaleArray = [None, '']
intake_GeometryDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_4.OpacityArray = [None, '']
intake_GeometryDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_4.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_4.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_4.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_4 = Show(plug, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_4.Representation = 'Surface'
plugDisplay_4.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_4.ColorArrayName = [None, '']
plugDisplay_4.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_4.Opacity = 0.7
plugDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_4.SelectOrientationVectors = 'None'
plugDisplay_4.ScaleFactor = 0.0010427969042211772
plugDisplay_4.SelectScaleArray = 'None'
plugDisplay_4.GlyphType = 'Arrow'
plugDisplay_4.GlyphTableIndexArray = 'None'
plugDisplay_4.GaussianRadius = 5.2139845211058853e-05
plugDisplay_4.SetScaleArray = [None, '']
plugDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_4.OpacityArray = [None, '']
plugDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_4.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_4.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_4.ExtractedBlockIndex = 1

# show data from head
headDisplay_1 = Show(head, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay_1.Representation = 'Surface'
headDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay_1.ColorArrayName = [None, '']
headDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay_1.Opacity = 0.25
headDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
headDisplay_1.SelectOrientationVectors = 'None'
headDisplay_1.ScaleFactor = 0.008899322897195817
headDisplay_1.SelectScaleArray = 'None'
headDisplay_1.GlyphType = 'Arrow'
headDisplay_1.GlyphTableIndexArray = 'None'
headDisplay_1.GaussianRadius = 0.0004449661448597908
headDisplay_1.SetScaleArray = [None, '']
headDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
headDisplay_1.OpacityArray = [None, '']
headDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
headDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
headDisplay_1.PolarAxes = 'PolarAxesRepresentation'
headDisplay_1.ScalarOpacityUnitDistance = 0.0016640944230168922
headDisplay_1.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_1 = Show(contour1, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_1.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_1.Specular = 1.0
contour1Display_1.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display_1.SpecularPower = 10.0
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = -2.0000000000000002e+298
contour1Display_1.SelectScaleArray = 'None'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'None'
contour1Display_1.GaussianRadius = -1e+297
contour1Display_1.SetScaleArray = [None, '']
contour1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_1.OpacityArray = [None, '']
contour1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_1.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_1.PolarAxes = 'PolarAxesRepresentation'

# show data from threshold1
threshold1Display_1 = Show(threshold1, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display_1.Representation = 'Surface'
threshold1Display_1.AmbientColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display_1.ColorArrayName = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_1.DiffuseColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display_1.LookupTable = dp_FROM_NOZZLELUT
threshold1Display_1.OSPRayScaleArray = 'dp_FROM_NOZZLE'
threshold1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display_1.SelectOrientationVectors = 'None'
threshold1Display_1.ScaleFactor = 0.008697206526994706
threshold1Display_1.SelectScaleArray = 'None'
threshold1Display_1.GlyphType = 'Arrow'
threshold1Display_1.GlyphTableIndexArray = 'None'
threshold1Display_1.GaussianRadius = 0.0004348603263497353
threshold1Display_1.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display_1.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display_1.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display_1.PolarAxes = 'PolarAxesRepresentation'
threshold1Display_1.ScalarOpacityFunction = dp_FROM_NOZZLEPWF
threshold1Display_1.ScalarOpacityUnitDistance = 0.0050929497409951735
threshold1Display_1.ExtractedBlockIndex = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView6'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_5 = Show(intake_Geometry, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intake_GeometryDisplay_5.Representation = 'Surface'
intake_GeometryDisplay_5.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_5.ColorArrayName = [None, '']
intake_GeometryDisplay_5.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
intake_GeometryDisplay_5.Opacity = 0.25
intake_GeometryDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
intake_GeometryDisplay_5.SelectOrientationVectors = 'None'
intake_GeometryDisplay_5.ScaleFactor = 0.020157745480537417
intake_GeometryDisplay_5.SelectScaleArray = 'None'
intake_GeometryDisplay_5.GlyphType = 'Arrow'
intake_GeometryDisplay_5.GlyphTableIndexArray = 'None'
intake_GeometryDisplay_5.GaussianRadius = 0.0010078872740268707
intake_GeometryDisplay_5.SetScaleArray = [None, '']
intake_GeometryDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_5.OpacityArray = [None, '']
intake_GeometryDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
intake_GeometryDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
intake_GeometryDisplay_5.PolarAxes = 'PolarAxesRepresentation'
intake_GeometryDisplay_5.ScalarOpacityUnitDistance = 0.002310755212500419
intake_GeometryDisplay_5.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_5 = Show(plug, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_5.Representation = 'Surface'
plugDisplay_5.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_5.ColorArrayName = [None, '']
plugDisplay_5.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_5.Opacity = 0.7
plugDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_5.SelectOrientationVectors = 'None'
plugDisplay_5.ScaleFactor = 0.0010427969042211772
plugDisplay_5.SelectScaleArray = 'None'
plugDisplay_5.GlyphType = 'Arrow'
plugDisplay_5.GlyphTableIndexArray = 'None'
plugDisplay_5.GaussianRadius = 5.2139845211058853e-05
plugDisplay_5.SetScaleArray = [None, '']
plugDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_5.OpacityArray = [None, '']
plugDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_5.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_5.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_5.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_2 = Show(contour1, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_2.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_2.Specular = 1.0
contour1Display_2.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display_2.SpecularPower = 10.0
contour1Display_2.OSPRayScaleArray = 'G_EQN_TRANSPORT'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'G_EQN_TRANSPORT'
contour1Display_2.ScaleFactor = 0.0025496815331280233
contour1Display_2.SelectScaleArray = 'G_EQN_TRANSPORT'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
contour1Display_2.GaussianRadius = 0.00012748407665640117
contour1Display_2.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_2.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_2.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from threshold1
threshold1Display_2 = Show(threshold1, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display_2.Representation = 'Surface'
threshold1Display_2.AmbientColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display_2.ColorArrayName = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_2.DiffuseColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display_2.LookupTable = dp_FROM_NOZZLELUT
threshold1Display_2.OSPRayScaleArray = 'dp_FROM_NOZZLE'
threshold1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display_2.SelectOrientationVectors = 'None'
threshold1Display_2.ScaleFactor = 0.008697206526994706
threshold1Display_2.SelectScaleArray = 'None'
threshold1Display_2.GlyphType = 'Arrow'
threshold1Display_2.GlyphTableIndexArray = 'None'
threshold1Display_2.GaussianRadius = 0.0004348603263497353
threshold1Display_2.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display_2.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display_2.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display_2.PolarAxes = 'PolarAxesRepresentation'
threshold1Display_2.ScalarOpacityFunction = dp_FROM_NOZZLEPWF
threshold1Display_2.ScalarOpacityUnitDistance = 0.0050929497409951735
threshold1Display_2.ExtractedBlockIndex = 1

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [12.138646125793457, 0.0, 0.5, 0.0, 270.4157430191116, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTPWF = GetOpacityTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTPWF.Points = [-0.10000014305114746, 0.0, 0.5, 0.0, -0.0009433941449970007, 1.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
g_EQN_TRANSPORTPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(intake_FrontStreamTracer)
# ----------------------------------------------------------------

SaveScreenshot(filename, layout1)
SaveScreenshot('/ccs/home/benjha/cmb124/everest/test.png', layout1_1, SaveAllViews=1,
    ImageResolution=[1920, 1080])
