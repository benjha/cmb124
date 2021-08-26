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

filename = 'LES4ECE_' + str(sys.argv[4]) + '_' + str(sys.argv[1]).zfill(4) + '.png'
dt = int(sys.argv[1])

#image resolution
res_x = int(sys.argv[2])
res_y = int(sys.argv[3])

#number of streamlines per source
n_streams = 99

#streamline source radius
radius = 0.014

#streamline width
s_width = 1.0

#file name to load
dataFileName='/gpfs/alpine/proj-shared/cmb124/paraview_files/' + str(sys.argv[4]) + '/pv.pvd'
print ('Loading ' + dataFileName)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [639, 663]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0038862526416778564, 0.0, -0.004494160413742065]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.001643460034725491, -0.380329863505669, -0.03162601505484531]
renderView1.CameraFocalPoint = [-0.001643460034725491, 0.0, -0.03162601505484531]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.098812199677732
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
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [365, 663]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.04728114977478981, 0.0, -0.004494160413742065]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [-0.5067509234783554, 0.0004465911591551933, -0.03466201398994453]
renderView3.CameraFocalPoint = [0.04728114977478981, 0.0004465911591551933, -0.03466201398994453]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 0.11749978506151411
renderView3.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView3.EnableRayTracing = 1
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.AmbientSamples = 1
renderView3.SamplesPerPixel = 16
renderView3.Denoise = 0
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [524, 663]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.04728114977478981, 0.0, -0.004494160413742065]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [0.0029265009251664086, -0.00016296891479192642, 0.18161212738187246]
renderView4.CameraFocalPoint = [0.0029265009251664086, -0.00016296891479192642, -0.03199122058960833]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 0.08094220416657892
renderView4.Background = [0.9411764705882353, 0.9411764705882353, 0.9411764705882353]
renderView4.EnableRayTracing = 1
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.AmbientSamples = 1
renderView4.SamplesPerPixel = 16
renderView4.Denoise = 0
renderView4.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.415929)
layout1.AssignView(1, renderView1)
layout1.SplitHorizontal(2, 0.410693)
layout1.AssignView(5, renderView3)
layout1.AssignView(6, renderView4)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView4)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVD Reader'
pvpvd = PVDReader(FileName=dataFileName)
pvpvd.CellArrays = ['G_EQN_TRANSPORT', 'TEMPERATURE', 'velocity']

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(Input=pvpvd)
extractTimeSteps1.TimeStepIndices = [dt]
#extractTimeSteps1.TimeStepRange = [0, 698]

# create a new 'Extract Block'
intakeExhaust_Geometry = ExtractBlock(Input=extractTimeSteps1)
intakeExhaust_Geometry.BlockIndices = [6, 23, 5, 22, 21, 20, 8, 15, 14, 13, 12, 3, 19, 17, 7, 16]
intakeExhaust_Geometry.MaintainStructure = 1

# create a new 'Extract Block'
intake_Geometry = ExtractBlock(Input=intakeExhaust_Geometry)
intake_Geometry.BlockIndices = [8, 7, 6, 5, 4, 3, 1, 10, 9]

# create a new 'Extract Block'
plug = ExtractBlock(Input=intake_Geometry)
plug.BlockIndices = [3, 2]

# create a new 'Extract Block'
head = ExtractBlock(Input=intakeExhaust_Geometry)
head.BlockIndices = [2]

# create a new 'Extract Block'
cell = ExtractBlock(Input=extractTimeSteps1)
cell.BlockIndices = [1]

# create a new 'Stream Tracer'
exhaust_FrontStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
exhaust_FrontStreamTracer.Vectors = ['CELLS', 'velocity']
exhaust_FrontStreamTracer.IntegrationDirection = 'FORWARD'
exhaust_FrontStreamTracer.InitialStepLength = 0.1
exhaust_FrontStreamTracer.MinimumStepLength = 0.09
exhaust_FrontStreamTracer.MaximumStepLength = 0.9
exhaust_FrontStreamTracer.MaximumStreamlineLength = 4.0
exhaust_FrontStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
exhaust_FrontStreamTracer.SeedType.Center = [-0.0213827, -0.0187533, 0.0015676188973778454]
exhaust_FrontStreamTracer.SeedType.NumberOfPoints = n_streams
exhaust_FrontStreamTracer.SeedType.Radius = radius

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

# create a new 'Stream Tracer'
intake_FrontStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
intake_FrontStreamTracer.Vectors = ['CELLS', 'velocity']
intake_FrontStreamTracer.IntegrationDirection = 'FORWARD'
intake_FrontStreamTracer.InitialStepLength = 0.1
intake_FrontStreamTracer.MinimumStepLength = 0.09
intake_FrontStreamTracer.MaximumStepLength = 0.9
intake_FrontStreamTracer.MaximumStreamlineLength = 4.0
intake_FrontStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
intake_FrontStreamTracer.SeedType.Center = [0.014318534497964766, -0.01875330655923476, 0.0015676188973778454]
intake_FrontStreamTracer.SeedType.NumberOfPoints = n_streams
intake_FrontStreamTracer.SeedType.Radius = radius

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
intake_BackStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
intake_BackStreamTracer.Vectors = ['CELLS', 'velocity']
intake_BackStreamTracer.IntegrationDirection = 'FORWARD'
intake_BackStreamTracer.InitialStepLength = 0.1
intake_BackStreamTracer.MinimumStepLength = 0.09
intake_BackStreamTracer.MaximumStepLength = 0.9
intake_BackStreamTracer.MaximumStreamlineLength = 4.0
intake_BackStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
intake_BackStreamTracer.SeedType.Center = [0.014318534497964766, 0.0187533, 0.0015676188973778454]
intake_BackStreamTracer.SeedType.NumberOfPoints = n_streams
intake_BackStreamTracer.SeedType.Radius = radius

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

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(Input=cell)
pythonAnnotation1.Expression = '"CA %3.2f" % Crank_Angle[0]'

# create a new 'Stream Tracer'
exhaust_BackStreamTracer = StreamTracer(Input=cell,
    SeedType='Point Source')
exhaust_BackStreamTracer.Vectors = ['CELLS', 'velocity']
exhaust_BackStreamTracer.IntegrationDirection = 'FORWARD'
exhaust_BackStreamTracer.InitialStepLength = 0.1
exhaust_BackStreamTracer.MinimumStepLength = 0.09
exhaust_BackStreamTracer.MaximumStepLength = 0.9
exhaust_BackStreamTracer.MaximumStreamlineLength = 4.0
exhaust_BackStreamTracer.ComputeVorticity = 0

# init the 'Point Source' selected for 'SeedType'
exhaust_BackStreamTracer.SeedType.Center = [-0.0213827, 0.0187533, 0.0015676188973778454]
exhaust_BackStreamTracer.SeedType.NumberOfPoints = n_streams
exhaust_BackStreamTracer.SeedType.Radius = radius

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

# create a new 'Cell Data to Point Data'
cell2Point_EQN_TRANS = CellDatatoPointData(Input=cell)
cell2Point_EQN_TRANS.ProcessAllArrays = 0
cell2Point_EQN_TRANS.CellDataArraytoprocess = ['G_EQN_TRANSPORT']

# create a new 'Contour'
contour1 = Contour(Input=cell2Point_EQN_TRANS)
contour1.ContourBy = ['POINTS', 'G_EQN_TRANSPORT']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

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
velocityLUT.RGBPoints = [0.0, 0.6705882352941176, 0.6705882352941176, 0.6705882352941176, 15.566036975078656, 1.0, 0.6666666666666666, 0.0, 33.96226539099357, 1.0, 0.6666666666666666, 0.0, 61.320752879971984, 0.0, 0.615686274509804, 0.0, 87.2641478384364, 0.06274509803921569, 0.7372549019607844, 1.0, 113.67924030707218, 0.6666666666666666, 0.0, 0.0, 150.0, 1.0, 0.0, 0.0]
velocityLUT.NumberOfTableValues = 6
velocityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay.Representation = 'Wireframe'
intake_FrontStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay.LineWidth = s_width
intake_FrontStreamTracerDisplay.OSPRayScaleArray = 'AngularVelocity'
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
intake_BackStreamTracerDisplay.LineWidth = s_width
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
exhaust_FrontStreamTracerDisplay.LineWidth = s_width
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

# show data from pythonAnnotation1
pythonAnnotation1Display = Show(pythonAnnotation1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
pythonAnnotation1Display.Color = [0.0, 0.0, 0.0]
pythonAnnotation1Display.Bold = 1
pythonAnnotation1Display.FontSize = 13
pythonAnnotation1Display.Position = [0.01, 0.9417426273458445]

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUT = GetColorTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTLUT.RGBPoints = [-0.10000014305114746, 0.050383, 0.029803, 0.527975, -0.09960794249010085, 0.063536, 0.028426, 0.533124, -0.09921584192919732, 0.075353, 0.027206, 0.538007, -0.09882364136815071, 0.086222, 0.026125, 0.542658, -0.09843154080724716, 0.096379, 0.025165, 0.547103, -0.09803934024620056, 0.10598, 0.024309, 0.551368, -0.09764723968529701, 0.115124, 0.023556, 0.555468, -0.09725503912425042, 0.123903, 0.022878, 0.559423, -0.09686283856320381, 0.132381, 0.022258, 0.56325, -0.09647073800230026, 0.140603, 0.021687, 0.566959, -0.09607853744125366, 0.148607, 0.021154, 0.570562, -0.09568643688035011, 0.156421, 0.020651, 0.574065, -0.09529423631930352, 0.16407, 0.020171, 0.577478, -0.09490213575839997, 0.171574, 0.019706, 0.580806, -0.09450993519735336, 0.17895, 0.019252, 0.584054, -0.09411773463630677, 0.186213, 0.018803, 0.587228, -0.09372563407540321, 0.193374, 0.018354, 0.59033, -0.0933334335143566, 0.200445, 0.017902, 0.593364, -0.09294133295345307, 0.207435, 0.017442, 0.596333, -0.09254913239240646, 0.21435, 0.016973, 0.599239, -0.09215703183150291, 0.221197, 0.016497, 0.602083, -0.09176483127045632, 0.227983, 0.016007, 0.604867, -0.09137263070940971, 0.234715, 0.015502, 0.607592, -0.09098053014850617, 0.241396, 0.014979, 0.610259, -0.09058832958745956, 0.248032, 0.014439, 0.612868, -0.09019622902655601, 0.254627, 0.013882, 0.615419, -0.08980402846550942, 0.261183, 0.013308, 0.617911, -0.08941192790460586, 0.267703, 0.012716, 0.620346, -0.08901972734355927, 0.274191, 0.012109, 0.622722, -0.08862762678265572, 0.280648, 0.011488, 0.625038, -0.08823542622160911, 0.287076, 0.010855, 0.627295, -0.08784322566056252, 0.293478, 0.010213, 0.62949, -0.08745112509965897, 0.299855, 0.009561, 0.631624, -0.08705892453861236, 0.30621, 0.008902, 0.633694, -0.08666682397770882, 0.312543, 0.008239, 0.6357, -0.08627462341666221, 0.318856, 0.007576, 0.63764, -0.08588252285575868, 0.32515, 0.006915, 0.639512, -0.08549032229471207, 0.331426, 0.006261, 0.641316, -0.08509812173366546, 0.337683, 0.005618, 0.643049, -0.08470602117276192, 0.343925, 0.004991, 0.64471, -0.08431382061171531, 0.35015, 0.004382, 0.646298, -0.08392172005081176, 0.356359, 0.003798, 0.64781, -0.08352951948976517, 0.362553, 0.003243, 0.649245, -0.08313741892886162, 0.368733, 0.002724, 0.650601, -0.08274521836781501, 0.374897, 0.002245, 0.651876, -0.08235301780676842, 0.381047, 0.001814, 0.653068, -0.08196091724586486, 0.387183, 0.001434, 0.654177, -0.08156871668481827, 0.393304, 0.001114, 0.655199, -0.08117661612391472, 0.399411, 0.000859, 0.656133, -0.08078441556286811, 0.405503, 0.000678, 0.656977, -0.08039231500196457, 0.41158, 0.000577, 0.65773, -0.08000011444091797, 0.417642, 0.000564, 0.65839, -0.07960791387987137, 0.423689, 0.000646, 0.658956, -0.07921581331896782, 0.429719, 0.000831, 0.659425, -0.07882361275792121, 0.435734, 0.001127, 0.659797, -0.07843151219701767, 0.441732, 0.00154, 0.660069, -0.07803931163597107, 0.447714, 0.00208, 0.66024, -0.07764721107506752, 0.453677, 0.002755, 0.66031, -0.07725501051402092, 0.459623, 0.003574, 0.660277, -0.07686280995297431, 0.46555, 0.004545, 0.660139, -0.07647070939207076, 0.471457, 0.005678, 0.659897, -0.07607850883102417, 0.477344, 0.00698, 0.659549, -0.07568640827012062, 0.48321, 0.00846, 0.659095, -0.07529420770907402, 0.489055, 0.010127, 0.658534, -0.07490210714817047, 0.494877, 0.01199, 0.657865, -0.07450990658712386, 0.500678, 0.014055, 0.657088, -0.07411770602607727, 0.506454, 0.016333, 0.656202, -0.07372560546517372, 0.512206, 0.018833, 0.655209, -0.07333340490412713, 0.517933, 0.021563, 0.654109, -0.07294130434322357, 0.523633, 0.024532, 0.652901, -0.07254910378217697, 0.529306, 0.027747, 0.651586, -0.07215700322127343, 0.534952, 0.031217, 0.650165, -0.07176480266022682, 0.54057, 0.03495, 0.64864, -0.07137260209918023, 0.546157, 0.038954, 0.64701, -0.07098050153827667, 0.551715, 0.043136, 0.645277, -0.07058830097723007, 0.557243, 0.047331, 0.643443, -0.07019620041632652, 0.562738, 0.051545, 0.641509, -0.06980399985527992, 0.568201, 0.055778, 0.639477, -0.06941189929437637, 0.573632, 0.060028, 0.637349, -0.06901969873332978, 0.579029, 0.064296, 0.635126, -0.06862759817242622, 0.584391, 0.068579, 0.632812, -0.06823539761137962, 0.589719, 0.072878, 0.630408, -0.06784319705033302, 0.595011, 0.07719, 0.627917, -0.06745109648942947, 0.600266, 0.081516, 0.625342, -0.06705889592838288, 0.605485, 0.085854, 0.622686, -0.06666679536747933, 0.610667, 0.090204, 0.619951, -0.06627459480643272, 0.615812, 0.094564, 0.61714, -0.06588249424552918, 0.620919, 0.098934, 0.614257, -0.06549029368448257, 0.625987, 0.103312, 0.611305, -0.06509809312343598, 0.631017, 0.107699, 0.608287, -0.06470599256253243, 0.636008, 0.112092, 0.605205, -0.06431379200148582, 0.640959, 0.116492, 0.602065, -0.06392169144058227, 0.645872, 0.120898, 0.598867, -0.06352949087953567, 0.650746, 0.125309, 0.595617, -0.06313739031863214, 0.65558, 0.129725, 0.592317, -0.06274518975758553, 0.660374, 0.134144, 0.588971, -0.06235298919653893, 0.665129, 0.138566, 0.585582, -0.061960888635635376, 0.669845, 0.142992, 0.582154, -0.061568688074588776, 0.674522, 0.147419, 0.578688, -0.061176587513685224, 0.67916, 0.151848, 0.575189, -0.06078438695263863, 0.683758, 0.156278, 0.57166, -0.06039228639173508, 0.688318, 0.160709, 0.568103, -0.06000008583068847, 0.69284, 0.165141, 0.564522, -0.05960788526964188, 0.697324, 0.169573, 0.560919, -0.059215784708738325, 0.701769, 0.174005, 0.557296, -0.058823584147691725, 0.706178, 0.178437, 0.553657, -0.05843148358678818, 0.710549, 0.182868, 0.550004, -0.05803928302574158, 0.714883, 0.187299, 0.546338, -0.05764718246483803, 0.719181, 0.191729, 0.542663, -0.05725498190379143, 0.723444, 0.196158, 0.538981, -0.05686278134274483, 0.72767, 0.200586, 0.535293, -0.056470680781841275, 0.731862, 0.205013, 0.531601, -0.05607848022079468, 0.736019, 0.209439, 0.527908, -0.05568637965989113, 0.740143, 0.213864, 0.524216, -0.05529417909884453, 0.744232, 0.218288, 0.520524, -0.054902078537940976, 0.748289, 0.222711, 0.516834, -0.05450987797689438, 0.752312, 0.227133, 0.513149, -0.054117677415847776, 0.756304, 0.231555, 0.509468, -0.05372557685494423, 0.760264, 0.235976, 0.505794, -0.05333337629389763, 0.764193, 0.240396, 0.502126, -0.05294127573299408, 0.76809, 0.244817, 0.498465, -0.05254907517194748, 0.771958, 0.249237, 0.494813, -0.05215697461104393, 0.775796, 0.253658, 0.491171, -0.05176477404999733, 0.779604, 0.258078, 0.487539, -0.051372573488950725, 0.783383, 0.2625, 0.483918, -0.05098047292804718, 0.787133, 0.266922, 0.480307, -0.05058827236700058, 0.790855, 0.271345, 0.476706, -0.05019617180609703, 0.794549, 0.27577, 0.473117, -0.049803971245050434, 0.798216, 0.280197, 0.469538, -0.049411870684146875, 0.801855, 0.284626, 0.465971, -0.049019670123100274, 0.805467, 0.289057, 0.462415, -0.048627569562196736, 0.809052, 0.293491, 0.45887, -0.048235369001150136, 0.812612, 0.297928, 0.455338, -0.047843168440103535, 0.816144, 0.302368, 0.451816, -0.04745106787919998, 0.819651, 0.306812, 0.448306, -0.04705886731815338, 0.823132, 0.311261, 0.444806, -0.04666676675724984, 0.826588, 0.315714, 0.441316, -0.04627456619620323, 0.830018, 0.320172, 0.437836, -0.045882465635299685, 0.833422, 0.324635, 0.434366, -0.045490265074253085, 0.836801, 0.329105, 0.430905, -0.045098064513206484, 0.840155, 0.33358, 0.427455, -0.04470596395230293, 0.843484, 0.338062, 0.424013, -0.04431376339125633, 0.846788, 0.342551, 0.420579, -0.04392166283035279, 0.850066, 0.347048, 0.417153, -0.04352946226930618, 0.853319, 0.351553, 0.413734, -0.043137361708402634, 0.856547, 0.356066, 0.410322, -0.042745161147356034, 0.85975, 0.360588, 0.406917, -0.04235296058630944, 0.862927, 0.365119, 0.403519, -0.04196086002540588, 0.866078, 0.36966, 0.400126, -0.04156865946435928, 0.869203, 0.374212, 0.396738, -0.041176558903455736, 0.872303, 0.378774, 0.393355, -0.04078435834240913, 0.875376, 0.383347, 0.389976, -0.04039225778150558, 0.878423, 0.387932, 0.3866, -0.04000005722045899, 0.881443, 0.392529, 0.383229, -0.03960785665941239, 0.884436, 0.397139, 0.37986, -0.03921575609850883, 0.887402, 0.401762, 0.376494, -0.03882355553746224, 0.89034, 0.406398, 0.37313, -0.03843145497655869, 0.89325, 0.411048, 0.369768, -0.03803925441551208, 0.896131, 0.415712, 0.366407, -0.03764715385460853, 0.898984, 0.420392, 0.363047, -0.03725495329356193, 0.901807, 0.425087, 0.359688, -0.03686275273251534, 0.904601, 0.429797, 0.356329, -0.036470652171611787, 0.907365, 0.434524, 0.35297, -0.03607845161056518, 0.910098, 0.439268, 0.34961, -0.03568635104966164, 0.9128, 0.444029, 0.346251, -0.035294150488615034, 0.915471, 0.448807, 0.34289, -0.03490204992771148, 0.918109, 0.453603, 0.339529, -0.03450984936666489, 0.920714, 0.458417, 0.336166, -0.034117648805618295, 0.923287, 0.463251, 0.332801, -0.03372554824471473, 0.925825, 0.468103, 0.329435, -0.033333347683668135, 0.928329, 0.472975, 0.326067, -0.0329412471227646, 0.930798, 0.477867, 0.322697, -0.032549046561717976, 0.933232, 0.48278, 0.319325, -0.03215694600081444, 0.93563, 0.487712, 0.315952, -0.031764745439767844, 0.93799, 0.492667, 0.312575, -0.03137254487872124, 0.940313, 0.497642, 0.309197, -0.030980444317817685, 0.942598, 0.502639, 0.305816, -0.03058824375677109, 0.944844, 0.507658, 0.302433, -0.03019614319586754, 0.947051, 0.512699, 0.299049, -0.029803942634820946, 0.949217, 0.517763, 0.295662, -0.029411842073917394, 0.951344, 0.52285, 0.292275, -0.029019641512870786, 0.953428, 0.52796, 0.288883, -0.028627540951967234, 0.95547, 0.533093, 0.28549, -0.02823534039092064, 0.957469, 0.53825, 0.282096, -0.027843139829874033, 0.959424, 0.543431, 0.278701, -0.027451039268970495, 0.961336, 0.548636, 0.275305, -0.027058838707923888, 0.963203, 0.553865, 0.271909, -0.026666738147020336, 0.965024, 0.559118, 0.268513, -0.026274537585973742, 0.966798, 0.564396, 0.265118, -0.02588243702507019, 0.968526, 0.5697, 0.261721, -0.025490236464023583, 0.970205, 0.575028, 0.258325, -0.02509803590297699, 0.971835, 0.580382, 0.254931, -0.024705935342073437, 0.973416, 0.585761, 0.25154, -0.024313734781026844, 0.974947, 0.591165, 0.248151, -0.023921634220123292, 0.976428, 0.596595, 0.244767, -0.023529433659076684, 0.977856, 0.602051, 0.241387, -0.023137333098173146, 0.979233, 0.607532, 0.238013, -0.02274513253712654, 0.980556, 0.613039, 0.234646, -0.02235293197607993, 0.981826, 0.618572, 0.231287, -0.021960831415176393, 0.983041, 0.624131, 0.227937, -0.0215686308541298, 0.984199, 0.629718, 0.224595, -0.021176530293226234, 0.985301, 0.63533, 0.221265, -0.02078432973217964, 0.986345, 0.640969, 0.217948, -0.020392229171276102, 0.987332, 0.646633, 0.214648, -0.02000002861022948, 0.98826, 0.652325, 0.211364, -0.019607828049182888, 0.989128, 0.658043, 0.2081, -0.01921572748827935, 0.989935, 0.663787, 0.204859, -0.018823526927232742, 0.990681, 0.669558, 0.201642, -0.01843142636632919, 0.991365, 0.675355, 0.198453, -0.018039225805282597, 0.991985, 0.681179, 0.195295, -0.017647125244379044, 0.992541, 0.68703, 0.19217, -0.017254924683332437, 0.993032, 0.692907, 0.189084, -0.016862724122285844, 0.993456, 0.69881, 0.186041, -0.01647062356138229, 0.993814, 0.704741, 0.183043, -0.016078423000335698, 0.994103, 0.710698, 0.180097, -0.015686322439432146, 0.994324, 0.716681, 0.177208, -0.015294121878385539, 0.994474, 0.722691, 0.174381, -0.014902021317482, 0.994553, 0.728728, 0.171622, -0.014509820756435393, 0.994561, 0.734791, 0.168938, -0.014117620195388786, 0.994495, 0.74088, 0.166335, -0.013725519634485248, 0.994355, 0.746995, 0.163821, -0.013333319073438654, 0.994141, 0.753137, 0.161404, -0.012941218512535088, 0.993851, 0.759304, 0.159092, -0.012549017951488495, 0.993482, 0.765499, 0.156891, -0.012156917390584943, 0.993033, 0.77172, 0.154808, -0.011764716829538335, 0.992505, 0.777967, 0.152855, -0.011372516268491742, 0.991897, 0.784239, 0.151042, -0.010980415707588204, 0.991209, 0.790537, 0.149377, -0.010588215146541596, 0.990439, 0.796859, 0.14787, -0.010196114585638044, 0.989587, 0.803205, 0.146529, -0.00980391402459145, 0.988648, 0.809579, 0.145357, -0.009411813463687899, 0.987621, 0.815978, 0.144363, -0.009019612902641305, 0.986509, 0.822401, 0.143557, -0.008627512341737753, 0.985314, 0.828846, 0.142945, -0.008235311780691146, 0.984031, 0.835315, 0.142528, -0.007843111219644552, 0.982653, 0.841812, 0.142303, -0.007451010658741, 0.98119, 0.848329, 0.142279, -0.007058810097694393, 0.979644, 0.854866, 0.142453, -0.006666709536790855, 0.977995, 0.861432, 0.142808, -0.006274508975744247, 0.976265, 0.868016, 0.143351, -0.005882408414840695, 0.974443, 0.874622, 0.144061, -0.005490207853794102, 0.97253, 0.88125, 0.144923, -0.0050980072927474945, 0.970533, 0.887896, 0.145919, -0.004705906731843942, 0.968443, 0.894564, 0.147014, -0.004313706170797349, 0.966271, 0.901249, 0.14818, -0.003921605609893797, 0.964021, 0.90795, 0.14937, -0.0035294050488472034, 0.961681, 0.914672, 0.15052, -0.0031373044879436512, 0.959276, 0.921407, 0.151566, -0.002745103926897044, 0.956808, 0.928152, 0.152409, -0.0023529033658504506, 0.954287, 0.934908, 0.152921, -0.0019608028049468984, 0.951726, 0.941671, 0.152925, -0.0015686022439002911, 0.949151, 0.948435, 0.152178, -0.0011765016829967528, 0.946602, 0.95519, 0.150328, -0.0007843011219501594, 0.944152, 0.961916, 0.146861, -0.0003922005610465934, 0.941896, 0.96859, 0.140956, 0.0, 0.940015, 0.975158, 0.131326]
g_EQN_TRANSPORTLUT.NanColor = [0.0, 1.0, 0.0]
g_EQN_TRANSPORTLUT.NumberOfTableValues = 1
g_EQN_TRANSPORTLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [1.0, 0.3333333333333333, 1.0]
contour1Display.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.DiffuseColor = [1.0, 0.3333333333333333, 1.0]
contour1Display.LookupTable = g_EQN_TRANSPORTLUT
contour1Display.InterpolateScalarsBeforeMapping = 0
contour1Display.Specular = 0.88
contour1Display.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display.Roughness = 0.22
contour1Display.RepeatTextures = 0
contour1Display.OSPRayScaleArray = 'G_EQN_TRANSPORT'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'G_EQN_TRANSPORT'
contour1Display.ScaleFactor = 4.941700026392937e-05
contour1Display.SelectScaleArray = 'G_EQN_TRANSPORT'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
contour1Display.GaussianRadius = 2.470850013196468e-06
contour1Display.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [-0.10000135004520416, 0.0, 0.5, 0.0, -0.09998609125614166, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [-0.10000135004520416, 0.0, 0.5, 0.0, -0.09998609125614166, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay = Show(exhaust_BackStreamTracer, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay.Representation = 'Wireframe'
exhaust_BackStreamTracerDisplay.ColorArrayName = ['POINTS', 'velocity']
exhaust_BackStreamTracerDisplay.LookupTable = velocityLUT
exhaust_BackStreamTracerDisplay.LineWidth = s_width
exhaust_BackStreamTracerDisplay.OSPRayScaleArray = 'IntegrationTime'
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

# setup the color legend parameters for each legend in this view

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.AutoOrient = 0
velocityLUTColorBar.WindowLocation = 'LowerLeftCorner'
velocityLUTColorBar.Position = [0.005095541401273885, 0.03359173126614989]
velocityLUTColorBar.Title = 'VELOCITY'
velocityLUTColorBar.ComponentTitle = ''
velocityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.UseCustomLabels = 1
velocityLUTColorBar.CustomLabels = [0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0]
velocityLUTColorBar.AddRangeLabels = 0
velocityLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
velocityLUTColorBar.ScalarBarThickness = 14
velocityLUTColorBar.ScalarBarLength = 0.5000000000000001

# set color bar visibility
velocityLUTColorBar.Visibility = 0

# show color legend
intake_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
intake_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
exhaust_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
exhaust_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from intake_Geometry
intake_GeometryDisplay_1 = Show(intake_Geometry, renderView3, 'UnstructuredGridRepresentation')

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
plugDisplay_1 = Show(plug, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plugDisplay_1.Representation = 'Surface'
plugDisplay_1.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_1.ColorArrayName = [None, '']
plugDisplay_1.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
plugDisplay_1.Opacity = 0.7
plugDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
plugDisplay_1.SelectOrientationVectors = 'None'
plugDisplay_1.ScaleFactor = 0.0010427969042211772
plugDisplay_1.SelectScaleArray = 'None'
plugDisplay_1.GlyphType = 'Arrow'
plugDisplay_1.GlyphTableIndexArray = 'None'
plugDisplay_1.GaussianRadius = 5.2139845211058853e-05
plugDisplay_1.SetScaleArray = [None, '']
plugDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
plugDisplay_1.OpacityArray = [None, '']
plugDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
plugDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
plugDisplay_1.PolarAxes = 'PolarAxesRepresentation'
plugDisplay_1.ScalarOpacityUnitDistance = 0.0004886308300994179
plugDisplay_1.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay_1 = Show(intake_FrontStreamTracer, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay_1.Representation = 'Wireframe'
intake_FrontStreamTracerDisplay_1.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay_1.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay_1.InterpolateScalarsBeforeMapping = 0
intake_FrontStreamTracerDisplay_1.LineWidth = s_width
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
intake_BackStreamTracerDisplay_1.InterpolateScalarsBeforeMapping = 0
intake_BackStreamTracerDisplay_1.LineWidth = s_width
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
exhaust_FrontStreamTracerDisplay_1.InterpolateScalarsBeforeMapping = 0
exhaust_FrontStreamTracerDisplay_1.LineWidth = s_width
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
exhaust_BackStreamTracerDisplay_1.InterpolateScalarsBeforeMapping = 0
exhaust_BackStreamTracerDisplay_1.LineWidth = s_width
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

# show data from contour1
contour1Display_1 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_1.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_1.Specular = 0.88
contour1Display_1.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display_1.RepeatTextures = 0
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
intake_GeometryDisplay_2 = Show(intake_Geometry, renderView4, 'UnstructuredGridRepresentation')

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
intake_GeometryDisplay_2.ScalarOpacityUnitDistance = 0.0021597388225030813
intake_GeometryDisplay_2.ExtractedBlockIndex = 1

# show data from plug
plugDisplay_2 = Show(plug, renderView4, 'UnstructuredGridRepresentation')

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
plugDisplay_2.ScalarOpacityUnitDistance = 0.0004946801360981299
plugDisplay_2.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay_2 = Show(intake_FrontStreamTracer, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontStreamTracerDisplay_2.Representation = 'Wireframe'
intake_FrontStreamTracerDisplay_2.ColorArrayName = ['POINTS', 'velocity']
intake_FrontStreamTracerDisplay_2.LookupTable = velocityLUT
intake_FrontStreamTracerDisplay_2.InterpolateScalarsBeforeMapping = 0
intake_FrontStreamTracerDisplay_2.LineWidth = s_width
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
intake_BackStreamTracerDisplay_2.InterpolateScalarsBeforeMapping = 0
intake_BackStreamTracerDisplay_2.LineWidth = s_width
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
exhaust_FrontStreamTracerDisplay_2.LineWidth = s_width
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
exhaust_BackStreamTracerDisplay_2.InterpolateScalarsBeforeMapping = 0
exhaust_BackStreamTracerDisplay_2.LineWidth = s_width
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

# show data from contour1
contour1Display_2 = Show(contour1, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_2.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_2.Specular = 0.88
contour1Display_2.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = -2.0000000000000002e+298
contour1Display_2.SelectScaleArray = 'None'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'None'
contour1Display_2.GaussianRadius = -1e+297
contour1Display_2.SetScaleArray = [None, '']
contour1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_2.OpacityArray = [None, '']
contour1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_2.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_2.PolarAxes = 'PolarAxesRepresentation'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTPWF = GetOpacityTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTPWF.Points = [-0.10000014305114746, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
g_EQN_TRANSPORTPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.0, 0.0, 0.5, 0.0, 150.0, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(intake_FrontStreamTracer)
# ----------------------------------------------------------------

SaveScreenshot(filename, layout1, SaveAllViews=1,
    ImageResolution=[res_x, res_y])

