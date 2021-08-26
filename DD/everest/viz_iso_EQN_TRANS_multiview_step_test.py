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

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1881, 1095]
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
renderView2.ViewSize = [1878, 1062]
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
renderView3.ViewSize = [804, 1095]
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
renderView4.ViewSize = [1149, 1095]
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
renderView5.ViewSize = [813, 1062]
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
renderView6.ViewSize = [1143, 1062]
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

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView6)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Text'
low = Text()
low.Text = 'Low'

# create a new 'PVD Reader'
pvpvd = PVDReader(FileName='/gpfs/alpine/proj-shared/cmb124/paraview_files/gEqnPlusKinetics_b1_14_b3_6_LES_map_b1_16_cycle2/pv.pvd')
pvpvd.CellArrays = ['G_EQN_TRANSPORT', 'TEMPERATURE', 'velocity']

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(Input=pvpvd)
extractTimeSteps1.TimeStepIndices = [87]
extractTimeSteps1.TimeStepRange = [0, 503]

# create a new 'Extract Block'
cell = ExtractBlock(Input=extractTimeSteps1)
cell.BlockIndices = [1]

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(Input=cell)
pythonAnnotation1.Expression = '"CA %3.3f" % Crank_Angle[0]'

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
exhaust_FrontStreamTracer.SeedType.NumberOfPoints = 10
exhaust_FrontStreamTracer.SeedType.Radius = 0.02

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

# create a new 'Cell Data to Point Data'
cell2Point_EQN_TRANS = CellDatatoPointData(Input=cell)
cell2Point_EQN_TRANS.ProcessAllArrays = 0
cell2Point_EQN_TRANS.CellDataArraytoprocess = ['G_EQN_TRANSPORT']

# create a new 'Contour'
contour1 = Contour(Input=cell2Point_EQN_TRANS)
contour1.ContourBy = ['POINTS', 'G_EQN_TRANSPORT']
contour1.Isosurfaces = [0.0]
contour1.PointMergeMethod = 'Uniform Binning'

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
exhaust_BackStreamTracer.SeedType.NumberOfPoints = 10
exhaust_BackStreamTracer.SeedType.Radius = 0.02

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
intake_FrontStreamTracer.SeedType.NumberOfPoints = 10
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

# create a new 'Extract Block'
parcel = ExtractBlock(Input=extractTimeSteps1)
parcel.BlockIndices = [2]

# create a new 'Threshold'
threshold1 = Threshold(Input=parcel)
threshold1.Scalars = ['POINTS', 'dp_TEMP']
threshold1.ThresholdRange = [0.0, 390.0]

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
high = Text()
high.Text = 'High'

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
intake_BackStreamTracer.SeedType.NumberOfPoints = 10
intake_BackStreamTracer.SeedType.Radius = 0.022

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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from pvpvd
pvpvdDisplay = Show(pvpvd, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.AutomaticRescaleRangeMode = 'Never'
velocityLUT.RGBPoints = [12.138645935859405, 0.278431372549, 0.278431372549, 0.858823529412, 49.072270818764466, 0.0, 0.0, 0.360784313725, 85.74761860458625, 0.0, 1.0, 1.0, 122.9395205845746, 0.0, 0.501960784314, 0.0, 159.61486837039638, 1.0, 1.0, 0.0, 196.54849325330144, 1.0, 0.380392156863, 0.0, 233.4821181362065, 0.419607843137, 0.0, 0.0, 270.4157430191116, 0.878431372549, 0.301960784314, 0.301960784314]
velocityLUT.ColorSpace = 'RGB'
velocityLUT.Discretize = 0
velocityLUT.NumberOfTableValues = 6
velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [12.138646125793457, 0.0, 0.5, 0.0, 270.4157430191116, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pvpvdDisplay.Representation = 'Surface'
pvpvdDisplay.ColorArrayName = ['CELLS', 'velocity']
pvpvdDisplay.LookupTable = velocityLUT
pvpvdDisplay.Opacity = 0.25
pvpvdDisplay.Specular = 0.5
pvpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pvpvdDisplay.SelectOrientationVectors = 'None'
pvpvdDisplay.ScaleFactor = 0.043956448137760167
pvpvdDisplay.SelectScaleArray = 'None'
pvpvdDisplay.GlyphType = 'Arrow'
pvpvdDisplay.GlyphTableIndexArray = 'None'
pvpvdDisplay.GaussianRadius = 0.002197822406888008
pvpvdDisplay.SetScaleArray = [None, '']
pvpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pvpvdDisplay.OpacityArray = [None, '']
pvpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pvpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
pvpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
pvpvdDisplay.ScalarOpacityFunction = velocityPWF
pvpvdDisplay.ScalarOpacityUnitDistance = 0.003021972108855904
pvpvdDisplay.ExtractedBlockIndex = 1

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

# show data from cell
cellDisplay = Show(cell, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cellDisplay.Representation = 'Surface'
cellDisplay.ColorArrayName = ['CELLS', 'velocity']
cellDisplay.LookupTable = velocityLUT
cellDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cellDisplay.SelectOrientationVectors = 'None'
cellDisplay.ScaleFactor = 0.043956448137760167
cellDisplay.SelectScaleArray = 'None'
cellDisplay.GlyphType = 'Arrow'
cellDisplay.GlyphTableIndexArray = 'None'
cellDisplay.GaussianRadius = 0.002197822406888008
cellDisplay.SetScaleArray = [None, '']
cellDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cellDisplay.OpacityArray = [None, '']
cellDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cellDisplay.DataAxesGrid = 'GridAxesRepresentation'
cellDisplay.PolarAxes = 'PolarAxesRepresentation'
cellDisplay.ScalarOpacityFunction = velocityPWF
cellDisplay.ScalarOpacityUnitDistance = 0.004267292653194057
cellDisplay.ExtractedBlockIndex = 1

# show data from intake_FrontStreamTracer
intake_FrontStreamTracerDisplay = Show(intake_FrontStreamTracer, renderView1, 'GeometryRepresentation')

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

# show data from intake_FrontArrows
intake_FrontArrowsDisplay = Show(intake_FrontArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontArrowsDisplay.Representation = 'Surface'
intake_FrontArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay.ColorArrayName = ['POINTS', '']
intake_FrontArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_FrontArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay.SelectOrientationVectors = 'AngularVelocity'
intake_FrontArrowsDisplay.ScaleFactor = 13.32074661254883
intake_FrontArrowsDisplay.SelectScaleArray = 'AngularVelocity'
intake_FrontArrowsDisplay.GlyphType = 'Arrow'
intake_FrontArrowsDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_FrontArrowsDisplay.GaussianRadius = 0.6660373306274414
intake_FrontArrowsDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_FrontArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_FrontArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontArrowsDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontArrowsDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from intake_BackArrows
intake_BackArrowsDisplay = Show(intake_BackArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackArrowsDisplay.Representation = 'Surface'
intake_BackArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay.ColorArrayName = ['POINTS', '']
intake_BackArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay.OSPRayScaleArray = 'AngularVelocity'
intake_BackArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay.SelectOrientationVectors = 'AngularVelocity'
intake_BackArrowsDisplay.ScaleFactor = 0.017043457902962456
intake_BackArrowsDisplay.SelectScaleArray = 'AngularVelocity'
intake_BackArrowsDisplay.GlyphType = 'Arrow'
intake_BackArrowsDisplay.GlyphTableIndexArray = 'AngularVelocity'
intake_BackArrowsDisplay.GaussianRadius = 0.0008521728951481228
intake_BackArrowsDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
intake_BackArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
intake_BackArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
intake_BackArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackArrowsDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackArrowsDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

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

# show data from exhaust_FrontArrows
exhaust_FrontArrowsDisplay = Show(exhaust_FrontArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontArrowsDisplay.Representation = 'Surface'
exhaust_FrontArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay.ColorArrayName = ['POINTS', '']
exhaust_FrontArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay.OSPRayScaleArray = 'AngularVelocity'
exhaust_FrontArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay.SelectOrientationVectors = 'AngularVelocity'
exhaust_FrontArrowsDisplay.ScaleFactor = 0.0183842733502388
exhaust_FrontArrowsDisplay.SelectScaleArray = 'AngularVelocity'
exhaust_FrontArrowsDisplay.GlyphType = 'Arrow'
exhaust_FrontArrowsDisplay.GlyphTableIndexArray = 'AngularVelocity'
exhaust_FrontArrowsDisplay.GaussianRadius = 0.00091921366751194
exhaust_FrontArrowsDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
exhaust_FrontArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
exhaust_FrontArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontArrowsDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontArrowsDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from pythonAnnotation1
pythonAnnotation1Display = Show(pythonAnnotation1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
pythonAnnotation1Display.Color = [0.0, 0.0, 0.0]
pythonAnnotation1Display.Bold = 1
pythonAnnotation1Display.FontSize = 20
pythonAnnotation1Display.WindowLocation = 'AnyLocation'
pythonAnnotation1Display.Position = [0.02, 0.875]

# show data from cell2Point_EQN_TRANS
cell2Point_EQN_TRANSDisplay = Show(cell2Point_EQN_TRANS, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUT = GetColorTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTLUT.RGBPoints = [-0.10000014305114746, 0.0, 0.0, 0.5625, -0.08888902715659142, 0.0, 0.0, 1.0, -0.06349214082610607, 0.0, 1.0, 1.0, -0.05079372266089916, 0.5, 1.0, 0.5, -0.038095304495692255, 1.0, 1.0, 0.0, -0.012698418165206907, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0]
g_EQN_TRANSPORTLUT.ColorSpace = 'RGB'
g_EQN_TRANSPORTLUT.NanColor = [0.0, 1.0, 0.0]
g_EQN_TRANSPORTLUT.Discretize = 0
g_EQN_TRANSPORTLUT.NumberOfTableValues = 1
g_EQN_TRANSPORTLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTPWF = GetOpacityTransferFunction('G_EQN_TRANSPORT')
g_EQN_TRANSPORTPWF.Points = [-0.10000014305114746, 0.0, 0.5, 0.0, -0.0009433941449970007, 1.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
g_EQN_TRANSPORTPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
cell2Point_EQN_TRANSDisplay.Representation = 'Surface'
cell2Point_EQN_TRANSDisplay.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
cell2Point_EQN_TRANSDisplay.LookupTable = g_EQN_TRANSPORTLUT
cell2Point_EQN_TRANSDisplay.OSPRayScaleArray = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cell2Point_EQN_TRANSDisplay.SelectOrientationVectors = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay.ScaleFactor = 0.043956448137760167
cell2Point_EQN_TRANSDisplay.SelectScaleArray = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay.GlyphType = 'Arrow'
cell2Point_EQN_TRANSDisplay.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay.GaussianRadius = 0.002197822406888008
cell2Point_EQN_TRANSDisplay.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
cell2Point_EQN_TRANSDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cell2Point_EQN_TRANSDisplay.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
cell2Point_EQN_TRANSDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cell2Point_EQN_TRANSDisplay.DataAxesGrid = 'GridAxesRepresentation'
cell2Point_EQN_TRANSDisplay.PolarAxes = 'PolarAxesRepresentation'
cell2Point_EQN_TRANSDisplay.ScalarOpacityFunction = g_EQN_TRANSPORTPWF
cell2Point_EQN_TRANSDisplay.ScalarOpacityUnitDistance = 0.0042299717991679
cell2Point_EQN_TRANSDisplay.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cell2Point_EQN_TRANSDisplay.ScaleTransferFunction.Points = [-0.10000135004520416, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cell2Point_EQN_TRANSDisplay.OpacityTransferFunction.Points = [-0.10000135004520416, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# set separate color map
cell2Point_EQN_TRANSDisplay.UseSeparateColorMap = True

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [1.0, 0.3333333333333333, 1.0]
contour1Display.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display.DiffuseColor = [1.0, 0.3333333333333333, 1.0]
contour1Display.LookupTable = g_EQN_TRANSPORTLUT
contour1Display.InterpolateScalarsBeforeMapping = 0
contour1Display.Specular = 0.67
contour1Display.Luminosity = 35.0
contour1Display.Ambient = 0.24
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

# show data from exhaust_BackArrows
exhaust_BackArrowsDisplay = Show(exhaust_BackArrows, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackArrowsDisplay.Representation = 'Surface'
exhaust_BackArrowsDisplay.AmbientColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay.ColorArrayName = ['POINTS', '']
exhaust_BackArrowsDisplay.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackArrowsDisplay.ScaleFactor = 0.010298835672438146
exhaust_BackArrowsDisplay.SelectScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay.GlyphType = 'Arrow'
exhaust_BackArrowsDisplay.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackArrowsDisplay.GaussianRadius = 0.0005149417836219073
exhaust_BackArrowsDisplay.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackArrowsDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackArrowsDisplay.ScaleTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackArrowsDisplay.OpacityTransferFunction.Points = [-0.003939886180206704, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

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

# show data from head
headDisplay = Show(head, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay.Representation = 'Surface'
headDisplay.ColorArrayName = [None, '']
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
headDisplay.ScalarOpacityUnitDistance = 0.0016499601988645993
headDisplay.ExtractedBlockIndex = 1

# show data from extractTimeSteps1
extractTimeSteps1Display = Show(extractTimeSteps1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps1Display.Representation = 'Surface'
extractTimeSteps1Display.ColorArrayName = ['CELLS', 'velocity']
extractTimeSteps1Display.LookupTable = velocityLUT
extractTimeSteps1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps1Display.SelectOrientationVectors = 'None'
extractTimeSteps1Display.ScaleFactor = 0.043956448137760167
extractTimeSteps1Display.SelectScaleArray = 'None'
extractTimeSteps1Display.GlyphType = 'Arrow'
extractTimeSteps1Display.GlyphTableIndexArray = 'None'
extractTimeSteps1Display.GaussianRadius = 0.002197822406888008
extractTimeSteps1Display.SetScaleArray = [None, '']
extractTimeSteps1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps1Display.OpacityArray = [None, '']
extractTimeSteps1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps1Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps1Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps1Display.ScalarOpacityFunction = velocityPWF
extractTimeSteps1Display.ScalarOpacityUnitDistance = 0.003021972108855904
extractTimeSteps1Display.ExtractedBlockIndex = 1

# show data from threshold1
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = -2.0000000000000002e+298
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = -1e+297
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ExtractedBlockIndex = 1

# show data from parcel
parcelDisplay = Show(parcel, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
parcelDisplay.Representation = 'Surface'
parcelDisplay.ColorArrayName = [None, '']
parcelDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay.SelectOrientationVectors = 'None'
parcelDisplay.ScaleFactor = -2.0000000000000002e+298
parcelDisplay.SelectScaleArray = 'None'
parcelDisplay.GlyphType = 'Arrow'
parcelDisplay.GlyphTableIndexArray = 'None'
parcelDisplay.GaussianRadius = -1e+297
parcelDisplay.SetScaleArray = [None, '']
parcelDisplay.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay.OpacityArray = [None, '']
parcelDisplay.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay.ExtractedBlockIndex = 1

# setup the color legend parameters for each legend in this view

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# get color legend/bar for vtkBlockColorsLUT in view renderView1
vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
vtkBlockColorsLUTColorBar.WindowLocation = 'UpperLeftCorner'
vtkBlockColorsLUTColorBar.Position = [0.019754768392370572, 0.664572864321608]
vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
vtkBlockColorsLUTColorBar.ComponentTitle = ''

# set color bar visibility
vtkBlockColorsLUTColorBar.Visibility = 0

# get color transfer function/color map for 'TEMPERATURE'
tEMPERATURELUT = GetColorTransferFunction('TEMPERATURE')
tEMPERATURELUT.AutomaticRescaleRangeMode = 'Never'
tEMPERATURELUT.RGBPoints = [200.0, 0.0, 1.0, 1.0, 695.0, 0.0, 0.0, 1.0, 750.0, 0.0, 0.0, 0.501960784314, 805.0, 1.0, 0.0, 0.0, 1300.0, 1.0, 1.0, 0.0]
tEMPERATURELUT.ColorSpace = 'RGB'
tEMPERATURELUT.ScalarRangeInitialized = 1.0

# get color legend/bar for tEMPERATURELUT in view renderView1
tEMPERATURELUTColorBar = GetScalarBar(tEMPERATURELUT, renderView1)
tEMPERATURELUTColorBar.Title = 'TEMPERATURE'
tEMPERATURELUTColorBar.ComponentTitle = ''

# set color bar visibility
tEMPERATURELUTColorBar.Visibility = 0

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

# get color legend/bar for dp_FROM_NOZZLELUT in view renderView1
dp_FROM_NOZZLELUTColorBar = GetScalarBar(dp_FROM_NOZZLELUT, renderView1)
dp_FROM_NOZZLELUTColorBar.Title = 'dp_FROM_NOZZLE'
dp_FROM_NOZZLELUTColorBar.ComponentTitle = ''

# set color bar visibility
dp_FROM_NOZZLELUTColorBar.Visibility = 0

# get color transfer function/color map for 'dp_TEMP'
dp_TEMPLUT = GetColorTransferFunction('dp_TEMP')
dp_TEMPLUT.AutomaticRescaleRangeMode = 'Never'
dp_TEMPLUT.RGBPoints = [200.0, 0.0, 0.0, 0.0, 320.0, 0.901960784314, 0.0, 0.0, 440.0, 0.901960784314, 0.901960784314, 0.0, 500.0, 1.0, 1.0, 1.0]
dp_TEMPLUT.ColorSpace = 'RGB'
dp_TEMPLUT.NanColor = [0.0, 0.498039215686, 1.0]
dp_TEMPLUT.Discretize = 0
dp_TEMPLUT.NumberOfTableValues = 1
dp_TEMPLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for dp_TEMPLUT in view renderView1
dp_TEMPLUTColorBar = GetScalarBar(dp_TEMPLUT, renderView1)
dp_TEMPLUTColorBar.Position = [0.9125949922157044, 0.03870665684002139]
dp_TEMPLUTColorBar.Title = 'dp_TEMP'
dp_TEMPLUTColorBar.ComponentTitle = ''
dp_TEMPLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
dp_TEMPLUTColorBar.TitleFontSize = 12
dp_TEMPLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
dp_TEMPLUTColorBar.LabelFontSize = 12
dp_TEMPLUTColorBar.ScalarBarLength = 0.32999999999999996

# set color bar visibility
dp_TEMPLUTColorBar.Visibility = 0

# get color transfer function/color map for 'dp_velocity'
dp_velocityLUT = GetColorTransferFunction('dp_velocity')
dp_velocityLUT.RGBPoints = [1.0468732896140134e-07, 0.231373, 0.298039, 0.752941, 156.42537399011036, 0.865003, 0.865003, 0.865003, 312.8507478755334, 0.705882, 0.0156863, 0.14902]
dp_velocityLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for dp_velocityLUT in view renderView1
dp_velocityLUTColorBar = GetScalarBar(dp_velocityLUT, renderView1)
dp_velocityLUTColorBar.WindowLocation = 'UpperRightCorner'
dp_velocityLUTColorBar.Title = 'dp_velocity'
dp_velocityLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
dp_velocityLUTColorBar.Visibility = 0

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

# get color transfer function/color map for 'Crank_Angle'
crank_AngleLUT = GetColorTransferFunction('Crank_Angle')
crank_AngleLUT.RGBPoints = [250.04531860351562, 0.231373, 0.298039, 0.752941, 250.06094360351562, 0.865003, 0.865003, 0.865003, 250.07656860351562, 0.705882, 0.0156863, 0.14902]
crank_AngleLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for crank_AngleLUT in view renderView1
crank_AngleLUTColorBar = GetScalarBar(crank_AngleLUT, renderView1)
crank_AngleLUTColorBar.Title = 'Crank_Angle'
crank_AngleLUTColorBar.ComponentTitle = ''

# set color bar visibility
crank_AngleLUTColorBar.Visibility = 0

# get color legend/bar for g_EQN_TRANSPORTLUT in view renderView1
g_EQN_TRANSPORTLUTColorBar = GetScalarBar(g_EQN_TRANSPORTLUT, renderView1)
g_EQN_TRANSPORTLUTColorBar.Orientation = 'Horizontal'
g_EQN_TRANSPORTLUTColorBar.WindowLocation = 'AnyLocation'
g_EQN_TRANSPORTLUTColorBar.Position = [0.0, 0.6483930942895085]
g_EQN_TRANSPORTLUTColorBar.Title = 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUTColorBar.ComponentTitle = ''
g_EQN_TRANSPORTLUTColorBar.ScalarBarLength = 0.32999999999999985

# set color bar visibility
g_EQN_TRANSPORTLUTColorBar.Visibility = 0

# get separate color transfer function/color map for 'G_EQN_TRANSPORT'
separate_contour1Display_G_EQN_TRANSPORTLUT = GetColorTransferFunction('G_EQN_TRANSPORT', contour1Display, separate=True)
separate_contour1Display_G_EQN_TRANSPORTLUT.RGBPoints = [-0.019999999552965164, 0.908659, 0.604013, 0.581857, -0.006679999850690364, 0.908659, 0.604013, 0.581857, 0.0066399998515844355, 1.0, 0.862745, 0.0, 0.019999999552965164, 0.0, 0.695201, 0.0]
separate_contour1Display_G_EQN_TRANSPORTLUT.ColorSpace = 'Step'
separate_contour1Display_G_EQN_TRANSPORTLUT.NanColor = [0.803922, 0.0, 0.803922]
separate_contour1Display_G_EQN_TRANSPORTLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_contour1Display_G_EQN_TRANSPORTLUT in view renderView1
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar = GetScalarBar(separate_contour1Display_G_EQN_TRANSPORTLUT, renderView1)
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.AutoOrient = 0
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.WindowLocation = 'LowerLeftCorner'
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.Position = [0.0030441400304414, 0.013404825737265416]
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.Title = 'G_EQN_TRANSPORT'
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.ComponentTitle = ''
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.TitleFontSize = 12
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.LabelFontSize = 12
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.ScalarBarThickness = 14
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.ScalarBarLength = 0.3

# set color bar visibility
separate_contour1Display_G_EQN_TRANSPORTLUTColorBar.Visibility = 0

# get color transfer function/color map for 'dp_RADIUS'
dp_RADIUSLUT = GetColorTransferFunction('dp_RADIUS')
dp_RADIUSLUT.RGBPoints = [1.3129704257153207e-07, 0.231373, 0.298039, 0.752941, 0.00012156123312934142, 0.865003, 0.865003, 0.865003, 0.0002429911692161113, 0.705882, 0.0156863, 0.14902]
dp_RADIUSLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for dp_RADIUSLUT in view renderView1
dp_RADIUSLUTColorBar = GetScalarBar(dp_RADIUSLUT, renderView1)
dp_RADIUSLUTColorBar.Position = [0.9237458193979933, 0.0160857908847185]
dp_RADIUSLUTColorBar.Title = 'dp_RADIUS'
dp_RADIUSLUTColorBar.ComponentTitle = ''
dp_RADIUSLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
dp_RADIUSLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# set color bar visibility
dp_RADIUSLUTColorBar.Visibility = 0

# get color transfer function/color map for 'dp_TEMP'
dp_TEMPLUT_1 = GetColorTransferFunction('dp_TEMP')
dp_TEMPLUT_1.RGBPoints = [306.0483093261719, 0.940015, 0.975158, 0.131326, 306.9234372940063, 0.941896, 0.96859, 0.140956, 307.7983421287537, 0.944152, 0.961916, 0.146861, 308.6734700965881, 0.946602, 0.95519, 0.150328, 309.5483749313354, 0.949151, 0.948435, 0.152178, 310.42350289916993, 0.951726, 0.941671, 0.152925, 311.29840773391726, 0.954287, 0.934908, 0.152921, 312.1735357017517, 0.956808, 0.928152, 0.152409, 313.04866366958623, 0.959276, 0.921407, 0.151566, 313.9235685043335, 0.961681, 0.914672, 0.15052, 314.79869647216793, 0.964021, 0.90795, 0.14937, 315.6736013069153, 0.966271, 0.901249, 0.14818, 316.54872927474975, 0.968443, 0.894564, 0.147014, 317.4236341094971, 0.970533, 0.887896, 0.145919, 318.29876207733156, 0.97253, 0.88125, 0.144923, 319.173890045166, 0.974443, 0.874622, 0.144061, 320.0487948799134, 0.976265, 0.868016, 0.143351, 320.9239228477478, 0.977995, 0.861432, 0.142808, 321.7988276824951, 0.979644, 0.854866, 0.142453, 322.67395565032956, 0.98119, 0.848329, 0.142279, 323.54886048507694, 0.982653, 0.841812, 0.142303, 324.4239884529114, 0.984031, 0.835315, 0.142528, 325.2991164207459, 0.985314, 0.828846, 0.142945, 326.17402125549313, 0.986509, 0.822401, 0.143557, 327.0491492233277, 0.987621, 0.815978, 0.144363, 327.924054058075, 0.988648, 0.809579, 0.145357, 328.79918202590943, 0.989587, 0.803205, 0.146529, 329.67408686065676, 0.990439, 0.796859, 0.14787, 330.54921482849124, 0.991209, 0.790537, 0.149377, 331.4241196632385, 0.991897, 0.784239, 0.151042, 332.29924763107294, 0.992505, 0.777967, 0.152855, 333.1743755989075, 0.993033, 0.77172, 0.154808, 334.04928043365476, 0.993482, 0.765499, 0.156891, 334.92440840148925, 0.993851, 0.759304, 0.159092, 335.79931323623657, 0.994141, 0.753137, 0.161404, 336.67444120407106, 0.994355, 0.746995, 0.163821, 337.5493460388184, 0.994495, 0.74088, 0.166335, 338.4244740066528, 0.994561, 0.734791, 0.168938, 339.29960197448725, 0.994553, 0.728728, 0.171622, 340.1745068092346, 0.994474, 0.722691, 0.174381, 341.0496347770691, 0.994324, 0.716681, 0.177208, 341.92453961181644, 0.994103, 0.710698, 0.180097, 342.79966757965093, 0.993814, 0.704741, 0.183043, 343.6745724143982, 0.993456, 0.69881, 0.186041, 344.54970038223263, 0.993032, 0.692907, 0.189084, 345.4248283500672, 0.992541, 0.68703, 0.19217, 346.29973318481444, 0.991985, 0.681179, 0.195295, 347.1748611526489, 0.991365, 0.675355, 0.198453, 348.04976598739626, 0.990681, 0.669558, 0.201642, 348.9248939552307, 0.989935, 0.663787, 0.204859, 349.799798789978, 0.989128, 0.658043, 0.2081, 350.6749267578125, 0.98826, 0.652325, 0.211364, 351.550054725647, 0.987332, 0.646633, 0.214648, 352.42495956039426, 0.986345, 0.640969, 0.217948, 353.3000875282288, 0.985301, 0.63533, 0.221265, 354.17499236297607, 0.984199, 0.629718, 0.224595, 355.0501203308105, 0.983041, 0.624131, 0.227937, 355.9250251655579, 0.981826, 0.618572, 0.231287, 356.8001531333923, 0.980556, 0.613039, 0.234646, 357.67528110122686, 0.979233, 0.607532, 0.238013, 358.5501859359741, 0.977856, 0.602051, 0.241387, 359.42531390380856, 0.976428, 0.596595, 0.244767, 360.30021873855594, 0.974947, 0.591165, 0.248151, 361.1753467063903, 0.973416, 0.585761, 0.25154, 362.05025154113764, 0.971835, 0.580382, 0.254931, 362.9253795089721, 0.970205, 0.575028, 0.258325, 363.8005074768067, 0.968526, 0.5697, 0.261721, 364.67541231155394, 0.966798, 0.564396, 0.265118, 365.55054027938843, 0.965024, 0.559118, 0.268513, 366.4254451141357, 0.963203, 0.553865, 0.271909, 367.30057308197024, 0.961336, 0.548636, 0.275305, 368.17547791671757, 0.959424, 0.543431, 0.278701, 369.050605884552, 0.957469, 0.53825, 0.282096, 369.92573385238643, 0.95547, 0.533093, 0.28549, 370.8006386871338, 0.953428, 0.52796, 0.288883, 371.67576665496824, 0.951344, 0.52285, 0.292275, 372.5506714897156, 0.949217, 0.517763, 0.295662, 373.4257994575501, 0.947051, 0.512699, 0.299049, 374.3007042922974, 0.944844, 0.507658, 0.302433, 375.1758322601318, 0.942598, 0.502639, 0.305816, 376.05073709487914, 0.940313, 0.497642, 0.309197, 376.92586506271357, 0.93799, 0.492667, 0.312575, 377.80099303054806, 0.93563, 0.487712, 0.315952, 378.67589786529544, 0.933232, 0.48278, 0.319325, 379.5510258331299, 0.930798, 0.477867, 0.322697, 380.42593066787725, 0.928329, 0.472975, 0.326067, 381.3010586357117, 0.925825, 0.468103, 0.329435, 382.175963470459, 0.923287, 0.463251, 0.332801, 383.05109143829344, 0.920714, 0.458417, 0.336166, 383.9262194061279, 0.918109, 0.453603, 0.339529, 384.8011242408752, 0.915471, 0.448807, 0.34289, 385.6762522087098, 0.9128, 0.444029, 0.346251, 386.551157043457, 0.910098, 0.439268, 0.34961, 387.4262850112915, 0.907365, 0.434524, 0.35297, 388.3011898460388, 0.904601, 0.429797, 0.356329, 389.17631781387325, 0.901807, 0.425087, 0.359688, 390.0514457817078, 0.898984, 0.420392, 0.363047, 390.9263506164551, 0.896131, 0.415712, 0.366407, 391.80147858428955, 0.89325, 0.411048, 0.369768, 392.6763834190368, 0.89034, 0.406398, 0.37313, 393.55151138687137, 0.887402, 0.401762, 0.376494, 394.42641622161864, 0.884436, 0.397139, 0.37986, 395.3015441894531, 0.881443, 0.392529, 0.383229, 396.1766721572876, 0.878423, 0.387932, 0.3866, 397.0515769920349, 0.875376, 0.383347, 0.389976, 397.9267049598694, 0.872303, 0.378774, 0.393355, 398.8016097946167, 0.869203, 0.374212, 0.396738, 399.6767377624511, 0.866078, 0.36966, 0.400126, 400.5516425971985, 0.862927, 0.365119, 0.403519, 401.42677056503294, 0.85975, 0.360588, 0.406917, 402.3018985328674, 0.856547, 0.356066, 0.410322, 403.1768033676147, 0.853319, 0.351553, 0.413734, 404.0519313354492, 0.850066, 0.347048, 0.417153, 404.9268361701965, 0.846788, 0.342551, 0.420579, 405.80196413803105, 0.843484, 0.338062, 0.424013, 406.6768689727783, 0.840155, 0.33358, 0.427455, 407.5519969406128, 0.836801, 0.329105, 0.430905, 408.4271249084473, 0.833422, 0.324635, 0.434366, 409.30202974319457, 0.830018, 0.320172, 0.437836, 410.17715771102905, 0.826588, 0.315714, 0.441316, 411.0520625457763, 0.823132, 0.311261, 0.444806, 411.92719051361087, 0.819651, 0.306812, 0.448306, 412.8020953483582, 0.816144, 0.302368, 0.451816, 413.6772233161926, 0.812612, 0.297928, 0.455338, 414.55235128402705, 0.809052, 0.293491, 0.45887, 415.4272561187744, 0.805467, 0.289057, 0.462415, 416.30238408660887, 0.801855, 0.284626, 0.465971, 417.17728892135625, 0.798216, 0.280197, 0.469538, 418.0524168891906, 0.794549, 0.27577, 0.473117, 418.927321723938, 0.790855, 0.271345, 0.476706, 419.8024496917725, 0.787133, 0.266922, 0.480307, 420.6773545265198, 0.783383, 0.2625, 0.483918, 421.55248249435425, 0.779604, 0.258078, 0.487539, 422.42761046218874, 0.775796, 0.253658, 0.491171, 423.302515296936, 0.771958, 0.249237, 0.494813, 424.17764326477055, 0.76809, 0.244817, 0.498465, 425.0525480995178, 0.764193, 0.240396, 0.502126, 425.9276760673523, 0.760264, 0.235976, 0.505794, 426.8025809020996, 0.756304, 0.231555, 0.509468, 427.67770886993407, 0.752312, 0.227133, 0.513149, 428.55283683776855, 0.748289, 0.222711, 0.516834, 429.4277416725158, 0.744232, 0.218288, 0.520524, 430.30286964035037, 0.740143, 0.213864, 0.524216, 431.1777744750977, 0.736019, 0.209439, 0.527908, 432.0529024429321, 0.731862, 0.205013, 0.531601, 432.9278072776794, 0.72767, 0.200586, 0.535293, 433.80293524551394, 0.723444, 0.196158, 0.538981, 434.6780632133483, 0.719181, 0.191729, 0.542663, 435.55296804809575, 0.714883, 0.187299, 0.546338, 436.42809601593024, 0.710549, 0.182868, 0.550004, 437.3030008506775, 0.706178, 0.178437, 0.553657, 438.1781288185119, 0.701769, 0.174005, 0.557296, 439.05303365325926, 0.697324, 0.169573, 0.560919, 439.9281616210938, 0.69284, 0.165141, 0.564522, 440.80328958892835, 0.688318, 0.160709, 0.568103, 441.67819442367556, 0.683758, 0.156278, 0.57166, 442.55332239151005, 0.67916, 0.151848, 0.575189, 443.4282272262574, 0.674522, 0.147419, 0.578688, 444.30335519409175, 0.669845, 0.142992, 0.582154, 445.1782600288391, 0.665129, 0.138566, 0.585582, 446.05338799667356, 0.660374, 0.134144, 0.588971, 446.92851596450805, 0.65558, 0.129725, 0.592317, 447.8034207992554, 0.650746, 0.125309, 0.595617, 448.67854876708986, 0.645872, 0.120898, 0.598867, 449.5534536018371, 0.640959, 0.116492, 0.602065, 450.4285815696717, 0.636008, 0.112092, 0.605205, 451.303486404419, 0.631017, 0.107699, 0.608287, 452.1786143722534, 0.625987, 0.103312, 0.611305, 453.05374234008787, 0.620919, 0.098934, 0.614257, 453.92864717483513, 0.615812, 0.094564, 0.61714, 454.8037751426697, 0.610667, 0.090204, 0.619951, 455.678679977417, 0.605485, 0.085854, 0.622686, 456.5538079452515, 0.600266, 0.081516, 0.625342, 457.42871277999876, 0.595011, 0.07719, 0.627917, 458.30384074783325, 0.589719, 0.072878, 0.630408, 459.17896871566774, 0.584391, 0.068579, 0.632812, 460.053873550415, 0.579029, 0.064296, 0.635126, 460.9290015182496, 0.573632, 0.060028, 0.637349, 461.8039063529968, 0.568201, 0.055778, 0.639477, 462.67903432083136, 0.562738, 0.051545, 0.641509, 463.55393915557863, 0.557243, 0.047331, 0.643443, 464.4290671234131, 0.551715, 0.043136, 0.645277, 465.3039719581604, 0.546157, 0.038954, 0.64701, 466.1790999259948, 0.54057, 0.03495, 0.64864, 467.0542278938293, 0.534952, 0.031217, 0.650165, 467.92913272857663, 0.529306, 0.027747, 0.651586, 468.8042606964111, 0.523633, 0.024532, 0.652901, 469.6791655311585, 0.517933, 0.021563, 0.654109, 470.5542934989928, 0.512206, 0.018833, 0.655209, 471.42919833374026, 0.506454, 0.016333, 0.656202, 472.30432630157475, 0.500678, 0.014055, 0.657088, 473.17945426940923, 0.494877, 0.01199, 0.657865, 474.05435910415656, 0.489055, 0.010127, 0.658534, 474.92948707199105, 0.48321, 0.00846, 0.659095, 475.8043919067384, 0.477344, 0.00698, 0.659549, 476.67951987457275, 0.471457, 0.005678, 0.659897, 477.5544247093201, 0.46555, 0.004545, 0.660139, 478.4295526771545, 0.459623, 0.003574, 0.660277, 479.304680644989, 0.453677, 0.002755, 0.66031, 480.17958547973626, 0.447714, 0.00208, 0.66024, 481.05471344757086, 0.441732, 0.00154, 0.660069, 481.9296182823181, 0.435734, 0.001127, 0.659797, 482.8047462501526, 0.429719, 0.000831, 0.659425, 483.6796510848999, 0.423689, 0.000646, 0.658956, 484.5547790527344, 0.417642, 0.000564, 0.65839, 485.42990702056886, 0.41158, 0.000577, 0.65773, 486.3048118553162, 0.405503, 0.000678, 0.656977, 487.17993982315056, 0.399411, 0.000859, 0.656133, 488.0548446578979, 0.393304, 0.001114, 0.655199, 488.9299726257325, 0.387183, 0.001434, 0.654177, 489.80487746047976, 0.381047, 0.001814, 0.653068, 490.6800054283142, 0.374897, 0.002245, 0.651876, 491.5551333961487, 0.368733, 0.002724, 0.650601, 492.4300382308961, 0.362553, 0.003243, 0.649245, 493.3051661987305, 0.356359, 0.003798, 0.64781, 494.1800710334778, 0.35015, 0.004382, 0.646298, 495.0551990013123, 0.343925, 0.004991, 0.64471, 495.9301038360596, 0.337683, 0.005618, 0.643049, 496.805231803894, 0.331426, 0.006261, 0.641316, 497.6803597717286, 0.32515, 0.006915, 0.639512, 498.5552646064759, 0.318856, 0.007576, 0.63764, 499.4303925743103, 0.312543, 0.008239, 0.6357, 500.30529740905763, 0.30621, 0.008902, 0.633694, 501.180425376892, 0.299855, 0.009561, 0.631624, 502.05533021163933, 0.293478, 0.010213, 0.62949, 502.9304581794738, 0.287076, 0.010855, 0.627295, 503.80558614730836, 0.280648, 0.011488, 0.625038, 504.68049098205563, 0.274191, 0.012109, 0.622722, 505.5556189498901, 0.267703, 0.012716, 0.620346, 506.43052378463744, 0.261183, 0.013308, 0.617911, 507.30565175247193, 0.254627, 0.013882, 0.615419, 508.18055658721926, 0.248032, 0.014439, 0.612868, 509.05568455505374, 0.241396, 0.014979, 0.610259, 509.93058938980107, 0.234715, 0.015502, 0.607592, 510.80571735763556, 0.227983, 0.016007, 0.604867, 511.68084532546993, 0.221197, 0.016497, 0.602083, 512.5557501602174, 0.21435, 0.016973, 0.599239, 513.4308781280517, 0.207435, 0.017442, 0.596333, 514.3057829627991, 0.200445, 0.017902, 0.593364, 515.1809109306336, 0.193374, 0.018354, 0.59033, 516.0558157653808, 0.186213, 0.018803, 0.587228, 516.9309437332154, 0.17895, 0.019252, 0.584054, 517.8060717010499, 0.171574, 0.019706, 0.580806, 518.6809765357971, 0.16407, 0.020171, 0.577478, 519.5561045036316, 0.156421, 0.020651, 0.574065, 520.4310093383789, 0.148607, 0.021154, 0.570562, 521.3061373062134, 0.140603, 0.021687, 0.566959, 522.1810421409607, 0.132381, 0.022258, 0.56325, 523.0561701087951, 0.123903, 0.022878, 0.559423, 523.9312980766297, 0.115124, 0.023556, 0.555468, 524.806202911377, 0.10598, 0.024309, 0.551368, 525.6813308792114, 0.096379, 0.025165, 0.547103, 526.5562357139587, 0.086222, 0.026125, 0.542658, 527.4313636817933, 0.075353, 0.027206, 0.538007, 528.3062685165405, 0.063536, 0.028426, 0.533124, 529.181396484375, 0.050383, 0.029803, 0.527975]
dp_TEMPLUT_1.NanColor = [0.0, 1.0, 0.0]
dp_TEMPLUT_1.NumberOfTableValues = 6
dp_TEMPLUT_1.ScalarRangeInitialized = 1.0

# get color legend/bar for dp_TEMPLUT_1 in view renderView1
dp_TEMPLUT_1ColorBar = GetScalarBar(dp_TEMPLUT_1, renderView1)
dp_TEMPLUT_1ColorBar.AutoOrient = 0
dp_TEMPLUT_1ColorBar.Position = [0.918010752688172, 0.013404825737265416]
dp_TEMPLUT_1ColorBar.Title = 'dp_TEMP'
dp_TEMPLUT_1ColorBar.ComponentTitle = ''
dp_TEMPLUT_1ColorBar.TitleColor = [0.0, 0.0, 0.0]
dp_TEMPLUT_1ColorBar.TitleFontSize = 12
dp_TEMPLUT_1ColorBar.LabelColor = [0.0, 0.0, 0.0]
dp_TEMPLUT_1ColorBar.LabelFontSize = 12
dp_TEMPLUT_1ColorBar.ScalarBarThickness = 14
dp_TEMPLUT_1ColorBar.ScalarBarLength = 0.3

# set color bar visibility
dp_TEMPLUT_1ColorBar.Visibility = 0

# get separate color transfer function/color map for 'velocity'
separate_intake_FrontStreamTracerDisplay_velocityLUT = GetColorTransferFunction('velocity', intake_FrontStreamTracerDisplay, separate=True)
separate_intake_FrontStreamTracerDisplay_velocityLUT.RGBPoints = [0.15321904838973519, 0.231373, 0.298039, 0.752941, 15.116993043675718, 0.865003, 0.865003, 0.865003, 30.080767038961703, 0.705882, 0.0156863, 0.14902]
separate_intake_FrontStreamTracerDisplay_velocityLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_intake_FrontStreamTracerDisplay_velocityLUT in view renderView1
separate_intake_FrontStreamTracerDisplay_velocityLUTColorBar = GetScalarBar(separate_intake_FrontStreamTracerDisplay_velocityLUT, renderView1)
separate_intake_FrontStreamTracerDisplay_velocityLUTColorBar.WindowLocation = 'UpperLeftCorner'
separate_intake_FrontStreamTracerDisplay_velocityLUTColorBar.Title = 'velocity'
separate_intake_FrontStreamTracerDisplay_velocityLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
separate_intake_FrontStreamTracerDisplay_velocityLUTColorBar.Visibility = 0

# get separate color transfer function/color map for 'velocity'
separate_intake_FrontArrowsDisplay_velocityLUT = GetColorTransferFunction('velocity', intake_FrontArrowsDisplay, separate=True)
separate_intake_FrontArrowsDisplay_velocityLUT.RGBPoints = [8.223022689899208, 0.231373, 0.298039, 0.752941, 55.1694831558061, 0.865003, 0.865003, 0.865003, 102.11594362171299, 0.705882, 0.0156863, 0.14902]
separate_intake_FrontArrowsDisplay_velocityLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for separate_intake_FrontArrowsDisplay_velocityLUT in view renderView1
separate_intake_FrontArrowsDisplay_velocityLUTColorBar = GetScalarBar(separate_intake_FrontArrowsDisplay_velocityLUT, renderView1)
separate_intake_FrontArrowsDisplay_velocityLUTColorBar.Title = 'velocity'
separate_intake_FrontArrowsDisplay_velocityLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
separate_intake_FrontArrowsDisplay_velocityLUTColorBar.Visibility = 0

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')
normalsLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.5000000528554036, 0.865003, 0.865003, 0.865003, 1.0000001057108072, 0.705882, 0.0156863, 0.14902]
normalsLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for normalsLUT in view renderView1
normalsLUTColorBar = GetScalarBar(normalsLUT, renderView1)
normalsLUTColorBar.WindowLocation = 'UpperLeftCorner'
normalsLUTColorBar.Title = 'Normals'
normalsLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
normalsLUTColorBar.Visibility = 0

# show color legend
pvpvdDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(pvpvd, renderView1)

# show color legend
cellDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(cell, renderView1)

# show color legend
intake_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
intake_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(intake_FrontArrows, renderView1)

# hide data in view
Hide(intake_BackArrows, renderView1)

# show color legend
exhaust_FrontStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(exhaust_FrontArrows, renderView1)

# hide data in view
Hide(cell2Point_EQN_TRANS, renderView1)

# hide data in view
Hide(contour1, renderView1)

# show color legend
exhaust_BackStreamTracerDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(exhaust_BackArrows, renderView1)

# hide data in view
Hide(head, renderView1)

# show color legend
extractTimeSteps1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(extractTimeSteps1, renderView1)

# hide data in view
Hide(threshold1, renderView1)

# hide data in view
Hide(parcel, renderView1)

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
contour1Display_1 = Show(contour1, renderView2, 'GeometryRepresentation')

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

# show data from pvpvd
pvpvdDisplay_1 = Show(pvpvd, renderView2, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'TEMPERATURE'
tEMPERATUREPWF = GetOpacityTransferFunction('TEMPERATURE')
tEMPERATUREPWF.Points = [200.0, 0.0, 0.5, 0.0, 1300.0, 1.0, 0.5, 0.0]
tEMPERATUREPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pvpvdDisplay_1.Representation = 'Surface'
pvpvdDisplay_1.ColorArrayName = ['CELLS', 'TEMPERATURE']
pvpvdDisplay_1.LookupTable = tEMPERATURELUT
pvpvdDisplay_1.OSPRayScaleArray = 'dp_FROM_NOZZLE'
pvpvdDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
pvpvdDisplay_1.SelectOrientationVectors = 'None'
pvpvdDisplay_1.ScaleFactor = 0.043956448137760167
pvpvdDisplay_1.SelectScaleArray = 'None'
pvpvdDisplay_1.GlyphType = 'Arrow'
pvpvdDisplay_1.GlyphTableIndexArray = 'None'
pvpvdDisplay_1.GaussianRadius = 0.002197822406888008
pvpvdDisplay_1.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
pvpvdDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
pvpvdDisplay_1.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
pvpvdDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
pvpvdDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
pvpvdDisplay_1.PolarAxes = 'PolarAxesRepresentation'
pvpvdDisplay_1.ScalarOpacityFunction = tEMPERATUREPWF
pvpvdDisplay_1.ScalarOpacityUnitDistance = 0.0030339935136965797
pvpvdDisplay_1.ExtractedBlockIndex = 1

# show data from parcel
parcelDisplay_1 = Show(parcel, renderView2, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'dp_TEMP'
dp_TEMPPWF = GetOpacityTransferFunction('dp_TEMP')
dp_TEMPPWF.Points = [200.0, 1.0, 0.5, 0.0, 350.0, 1.0, 0.5, 0.0, 500.0, 1.0, 0.5, 0.0, 500.0, 0.0, 0.5, 0.0]
dp_TEMPPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
parcelDisplay_1.Representation = 'Points'
parcelDisplay_1.ColorArrayName = ['POINTS', 'dp_TEMP']
parcelDisplay_1.LookupTable = dp_TEMPLUT
parcelDisplay_1.Interpolation = 'Flat'
parcelDisplay_1.Specular = 0.46
parcelDisplay_1.SpecularPower = 10.0
parcelDisplay_1.Luminosity = 18.0
parcelDisplay_1.Ambient = 0.16
parcelDisplay_1.Diffuse = 0.9
parcelDisplay_1.Roughness = 0.5
parcelDisplay_1.Metallic = 0.69
parcelDisplay_1.EdgeColor = [1.0, 1.0, 1.0]
parcelDisplay_1.OSPRayScaleArray = 'dp_TEMP'
parcelDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay_1.SelectOrientationVectors = 'None'
parcelDisplay_1.ScaleFactor = 0.015194140002131463
parcelDisplay_1.SelectScaleArray = 'None'
parcelDisplay_1.GlyphType = 'Arrow'
parcelDisplay_1.GlyphTableIndexArray = 'None'
parcelDisplay_1.GaussianRadius = 0.0007597070001065732
parcelDisplay_1.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay_1.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay_1.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay_1.ScalarOpacityFunction = dp_TEMPPWF
parcelDisplay_1.ScalarOpacityUnitDistance = 0.0055156914629405866
parcelDisplay_1.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
parcelDisplay_1.OSPRayScaleFunction.Points = [0.01, 0.0, 0.5, 0.0, 0.012375690555555556, 0.6145833134651184, 0.5, 0.0, 0.016160221111111112, 0.8333333134651184, 0.5, 0.0, 0.02, 1.0, 0.5, 0.0]

# show data from threshold1
threshold1Display_1 = Show(threshold1, renderView2, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'dp_FROM_NOZZLE'
dp_FROM_NOZZLEPWF = GetOpacityTransferFunction('dp_FROM_NOZZLE')
dp_FROM_NOZZLEPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
dp_FROM_NOZZLEPWF.ScalarRangeInitialized = 1

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

# show data from pythonAnnotation1
pythonAnnotation1Display_1 = Show(pythonAnnotation1, renderView2, 'TextSourceRepresentation')

# trace defaults for the display properties.
pythonAnnotation1Display_1.Color = [0.0, 0.0, 0.0]
pythonAnnotation1Display_1.WindowLocation = 'AnyLocation'
pythonAnnotation1Display_1.Position = [0.02, 0.87]

# setup the color legend parameters for each legend in this view

# get color legend/bar for dp_TEMPLUT in view renderView2
dp_TEMPLUTColorBar_1 = GetScalarBar(dp_TEMPLUT, renderView2)
dp_TEMPLUTColorBar_1.WindowLocation = 'LowerLeftCorner'
dp_TEMPLUTColorBar_1.Position = [0.8525754884547069, 0.088]
dp_TEMPLUTColorBar_1.Title = 'PARCEL TEMPERATURE'
dp_TEMPLUTColorBar_1.ComponentTitle = ''
dp_TEMPLUTColorBar_1.TitleColor = [0.0, 0.0, 0.0]
dp_TEMPLUTColorBar_1.LabelColor = [0.0, 0.0, 0.0]
dp_TEMPLUTColorBar_1.AddRangeLabels = 0
dp_TEMPLUTColorBar_1.TextPosition = 'Ticks left/bottom, annotations right/top'
dp_TEMPLUTColorBar_1.ScalarBarLength = 0.5

# set color bar visibility
dp_TEMPLUTColorBar_1.Visibility = 0

# get color legend/bar for dp_RADIUSLUT in view renderView2
dp_RADIUSLUTColorBar_1 = GetScalarBar(dp_RADIUSLUT, renderView2)
dp_RADIUSLUTColorBar_1.Title = 'dp_RADIUS'
dp_RADIUSLUTColorBar_1.ComponentTitle = ''

# set color bar visibility
dp_RADIUSLUTColorBar_1.Visibility = 0

# get color transfer function/color map for 'BOUND_TEMP'
bOUND_TEMPLUT = GetColorTransferFunction('BOUND_TEMP')
bOUND_TEMPLUT.RGBPoints = [393.0, 0.231373, 0.298039, 0.752941, 718.0, 0.865003, 0.865003, 0.865003, 1043.0, 0.705882, 0.0156863, 0.14902]
bOUND_TEMPLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for bOUND_TEMPLUT in view renderView2
bOUND_TEMPLUTColorBar = GetScalarBar(bOUND_TEMPLUT, renderView2)
bOUND_TEMPLUTColorBar.WindowLocation = 'UpperRightCorner'
bOUND_TEMPLUTColorBar.Title = 'BOUND_TEMP'
bOUND_TEMPLUTColorBar.ComponentTitle = ''

# set color bar visibility
bOUND_TEMPLUTColorBar.Visibility = 0

# get color legend/bar for tEMPERATURELUT in view renderView2
tEMPERATURELUTColorBar_1 = GetScalarBar(tEMPERATURELUT, renderView2)
tEMPERATURELUTColorBar_1.WindowLocation = 'AnyLocation'
tEMPERATURELUTColorBar_1.Position = [0.024866785079928892, 0.3973333333333332]
tEMPERATURELUTColorBar_1.Title = 'TEMPERATURE'
tEMPERATURELUTColorBar_1.ComponentTitle = ''
tEMPERATURELUTColorBar_1.TitleColor = [0.0, 0.0, 0.0]
tEMPERATURELUTColorBar_1.TitleFontSize = 14
tEMPERATURELUTColorBar_1.LabelColor = [0.0, 0.0, 0.0]
tEMPERATURELUTColorBar_1.LabelFontSize = 14
tEMPERATURELUTColorBar_1.AddRangeLabels = 0
tEMPERATURELUTColorBar_1.ScalarBarLength = 0.49266666666666636

# set color bar visibility
tEMPERATURELUTColorBar_1.Visibility = 0

# get color legend/bar for g_EQN_TRANSPORTLUT in view renderView2
g_EQN_TRANSPORTLUTColorBar_1 = GetScalarBar(g_EQN_TRANSPORTLUT, renderView2)
g_EQN_TRANSPORTLUTColorBar_1.Title = 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUTColorBar_1.ComponentTitle = ''

# set color bar visibility
g_EQN_TRANSPORTLUTColorBar_1.Visibility = 0

# get color legend/bar for dp_FROM_NOZZLELUT in view renderView2
dp_FROM_NOZZLELUTColorBar_1 = GetScalarBar(dp_FROM_NOZZLELUT, renderView2)
dp_FROM_NOZZLELUTColorBar_1.Position = [0.7489177489177489, 0.04269972451790634]
dp_FROM_NOZZLELUTColorBar_1.Title = 'dp_FROM_NOZZLE'
dp_FROM_NOZZLELUTColorBar_1.ComponentTitle = ''

# set color bar visibility
dp_FROM_NOZZLELUTColorBar_1.Visibility = 0

# get color transfer function/color map for 'dp_NUM_DROP'
dp_NUM_DROPLUT = GetColorTransferFunction('dp_NUM_DROP')
dp_NUM_DROPLUT.RGBPoints = [0.0036555055994540453, 0.231373, 0.298039, 0.752941, 1923232.751827753, 0.865003, 0.865003, 0.865003, 3846465.5, 0.705882, 0.0156863, 0.14902]
dp_NUM_DROPLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for dp_NUM_DROPLUT in view renderView2
dp_NUM_DROPLUTColorBar = GetScalarBar(dp_NUM_DROPLUT, renderView2)
dp_NUM_DROPLUTColorBar.Title = 'dp_NUM_DROP'
dp_NUM_DROPLUTColorBar.ComponentTitle = ''

# set color bar visibility
dp_NUM_DROPLUTColorBar.Visibility = 0

# get color legend/bar for dp_velocityLUT in view renderView2
dp_velocityLUTColorBar_1 = GetScalarBar(dp_velocityLUT, renderView2)
dp_velocityLUTColorBar_1.Title = 'dp_velocity'
dp_velocityLUTColorBar_1.ComponentTitle = 'Magnitude'

# set color bar visibility
dp_velocityLUTColorBar_1.Visibility = 0

# get color transfer function/color map for 'v_mag'
v_magLUT = GetColorTransferFunction('v_mag')
v_magLUT.RGBPoints = [4.708444910864552e-07, 0.231373, 0.298039, 0.752941, 17.78195174216174, 0.865003, 0.865003, 0.865003, 35.56390301347899, 0.705882, 0.0156863, 0.14902]
v_magLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for v_magLUT in view renderView2
v_magLUTColorBar = GetScalarBar(v_magLUT, renderView2)
v_magLUTColorBar.WindowLocation = 'AnyLocation'
v_magLUTColorBar.Position = [0.11688311688311698, 0.28099173553719]
v_magLUTColorBar.Title = 'v_mag'
v_magLUTColorBar.ComponentTitle = ''
v_magLUTColorBar.ScalarBarLength = 0.33000000000000035

# set color bar visibility
v_magLUTColorBar.Visibility = 0

# hide data in view
Hide(pvpvd, renderView2)

# hide data in view
Hide(parcel, renderView2)

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

# show data from intake_FrontArrows
intake_FrontArrowsDisplay_1 = Show(intake_FrontArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontArrowsDisplay_1.Representation = 'Surface'
intake_FrontArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_1.ColorArrayName = ['POINTS', '']
intake_FrontArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_FrontArrowsDisplay_1.ScaleFactor = 0.014322103932499886
intake_FrontArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_1.GlyphType = 'Arrow'
intake_FrontArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontArrowsDisplay_1.GaussianRadius = 0.0007161051966249943
intake_FrontArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontArrowsDisplay_1.ScaleTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontArrowsDisplay_1.OpacityTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

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

# show data from intake_BackArrows
intake_BackArrowsDisplay_1 = Show(intake_BackArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackArrowsDisplay_1.Representation = 'Surface'
intake_BackArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_1.ColorArrayName = [None, '']
intake_BackArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
intake_BackArrowsDisplay_1.ScaleFactor = 0.014297069981694221
intake_BackArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_1.GlyphType = 'Arrow'
intake_BackArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
intake_BackArrowsDisplay_1.GaussianRadius = 0.000714853499084711
intake_BackArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
intake_BackArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackArrowsDisplay_1.ScaleTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackArrowsDisplay_1.OpacityTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

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

# show data from exhaust_FrontArrows
exhaust_FrontArrowsDisplay_1 = Show(exhaust_FrontArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontArrowsDisplay_1.Representation = 'Surface'
exhaust_FrontArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_1.ColorArrayName = [None, '']
exhaust_FrontArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.ScaleFactor = 0.014079396799206735
exhaust_FrontArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.GlyphType = 'Arrow'
exhaust_FrontArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_1.GaussianRadius = 0.0007039698399603367
exhaust_FrontArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontArrowsDisplay_1.ScaleTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontArrowsDisplay_1.OpacityTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

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

# show data from exhaust_BackArrows
exhaust_BackArrowsDisplay_1 = Show(exhaust_BackArrows, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackArrowsDisplay_1.Representation = 'Surface'
exhaust_BackArrowsDisplay_1.AmbientColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_1.ColorArrayName = [None, '']
exhaust_BackArrowsDisplay_1.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_1.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_1.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.ScaleFactor = 0.014254055917263031
exhaust_BackArrowsDisplay_1.SelectScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.GlyphType = 'Arrow'
exhaust_BackArrowsDisplay_1.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_1.GaussianRadius = 0.0007127027958631516
exhaust_BackArrowsDisplay_1.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_1.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackArrowsDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackArrowsDisplay_1.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackArrowsDisplay_1.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_2 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_2.LookupTable = g_EQN_TRANSPORTLUT
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

# show data from head
headDisplay_1 = Show(head, renderView3, 'UnstructuredGridRepresentation')

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

# show data from cell2Point_EQN_TRANS
cell2Point_EQN_TRANSDisplay_1 = Show(cell2Point_EQN_TRANS, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cell2Point_EQN_TRANSDisplay_1.Representation = 'Surface'
cell2Point_EQN_TRANSDisplay_1.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
cell2Point_EQN_TRANSDisplay_1.LookupTable = g_EQN_TRANSPORTLUT
cell2Point_EQN_TRANSDisplay_1.OSPRayScaleArray = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
cell2Point_EQN_TRANSDisplay_1.SelectOrientationVectors = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay_1.ScaleFactor = 0.043956448137760167
cell2Point_EQN_TRANSDisplay_1.SelectScaleArray = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay_1.GlyphType = 'Arrow'
cell2Point_EQN_TRANSDisplay_1.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
cell2Point_EQN_TRANSDisplay_1.GaussianRadius = 0.002197822406888008
cell2Point_EQN_TRANSDisplay_1.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
cell2Point_EQN_TRANSDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
cell2Point_EQN_TRANSDisplay_1.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
cell2Point_EQN_TRANSDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
cell2Point_EQN_TRANSDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
cell2Point_EQN_TRANSDisplay_1.PolarAxes = 'PolarAxesRepresentation'
cell2Point_EQN_TRANSDisplay_1.ScalarOpacityFunction = g_EQN_TRANSPORTPWF
cell2Point_EQN_TRANSDisplay_1.ScalarOpacityUnitDistance = 0.004226090835482809
cell2Point_EQN_TRANSDisplay_1.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cell2Point_EQN_TRANSDisplay_1.ScaleTransferFunction.Points = [-0.10000014305114746, 0.0, 0.5, 0.0, -0.09999980032444, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cell2Point_EQN_TRANSDisplay_1.OpacityTransferFunction.Points = [-0.10000014305114746, 0.0, 0.5, 0.0, -0.09999980032444, 1.0, 0.5, 0.0]

# show data from pythonAnnotation1
pythonAnnotation1Display_2 = Show(pythonAnnotation1, renderView3, 'TextSourceRepresentation')

# show data from intakeExhaust_Geometry
intakeExhaust_GeometryDisplay_2 = Show(intakeExhaust_Geometry, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intakeExhaust_GeometryDisplay_2.Representation = 'Surface'
intakeExhaust_GeometryDisplay_2.ColorArrayName = [None, '']
intakeExhaust_GeometryDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_2.SelectOrientationVectors = 'None'
intakeExhaust_GeometryDisplay_2.ScaleFactor = 0.027035209536552432
intakeExhaust_GeometryDisplay_2.SelectScaleArray = 'None'
intakeExhaust_GeometryDisplay_2.GlyphType = 'Arrow'
intakeExhaust_GeometryDisplay_2.GlyphTableIndexArray = 'None'
intakeExhaust_GeometryDisplay_2.GaussianRadius = 0.0013517604768276215
intakeExhaust_GeometryDisplay_2.SetScaleArray = [None, '']
intakeExhaust_GeometryDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_2.OpacityArray = [None, '']
intakeExhaust_GeometryDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intakeExhaust_GeometryDisplay_2.PolarAxes = 'PolarAxesRepresentation'
intakeExhaust_GeometryDisplay_2.ScalarOpacityUnitDistance = 0.0022078937529100913
intakeExhaust_GeometryDisplay_2.ExtractedBlockIndex = 1

# setup the color legend parameters for each legend in this view

# get color legend/bar for velocityLUT in view renderView3
velocityLUTColorBar_1 = GetScalarBar(velocityLUT, renderView3)
velocityLUTColorBar_1.Title = 'velocity'
velocityLUTColorBar_1.ComponentTitle = 'Magnitude'

# set color bar visibility
velocityLUTColorBar_1.Visibility = 0

# get color legend/bar for g_EQN_TRANSPORTLUT in view renderView3
g_EQN_TRANSPORTLUTColorBar_2 = GetScalarBar(g_EQN_TRANSPORTLUT, renderView3)
g_EQN_TRANSPORTLUTColorBar_2.Title = 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUTColorBar_2.ComponentTitle = ''

# set color bar visibility
g_EQN_TRANSPORTLUTColorBar_2.Visibility = 0

# hide data in view
Hide(intake_FrontArrows, renderView3)

# hide data in view
Hide(intake_BackArrows, renderView3)

# hide data in view
Hide(exhaust_FrontArrows, renderView3)

# hide data in view
Hide(exhaust_BackArrows, renderView3)

# hide data in view
Hide(contour1, renderView3)

# hide data in view
Hide(cell2Point_EQN_TRANS, renderView3)

# hide data in view
Hide(intakeExhaust_Geometry, renderView3)

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

# show data from intake_FrontArrows
intake_FrontArrowsDisplay_2 = Show(intake_FrontArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_FrontArrowsDisplay_2.Representation = 'Surface'
intake_FrontArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_2.ColorArrayName = ['POINTS', '']
intake_FrontArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
intake_FrontArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_FrontArrowsDisplay_2.ScaleFactor = 0.014322103932499886
intake_FrontArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_FrontArrowsDisplay_2.GlyphType = 'Arrow'
intake_FrontArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_FrontArrowsDisplay_2.GaussianRadius = 0.0007161051966249943
intake_FrontArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_FrontArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_FrontArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_FrontArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_FrontArrowsDisplay_2.ScaleTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_FrontArrowsDisplay_2.OpacityTransferFunction.Points = [-0.004276378708688169, 0.0, 0.5, 0.0, 0.014827226264019767, 1.0, 0.5, 0.0]

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

# show data from intake_BackArrows
intake_BackArrowsDisplay_2 = Show(intake_BackArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
intake_BackArrowsDisplay_2.Representation = 'Surface'
intake_BackArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_2.ColorArrayName = [None, '']
intake_BackArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
intake_BackArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
intake_BackArrowsDisplay_2.ScaleFactor = 0.014297069981694221
intake_BackArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
intake_BackArrowsDisplay_2.GlyphType = 'Arrow'
intake_BackArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
intake_BackArrowsDisplay_2.GaussianRadius = 0.000714853499084711
intake_BackArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
intake_BackArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
intake_BackArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
intake_BackArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
intake_BackArrowsDisplay_2.ScaleTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
intake_BackArrowsDisplay_2.OpacityTransferFunction.Points = [-0.006420766937501416, 0.0, 0.5, 0.0, 0.04700008626400648, 1.0, 0.5, 0.0]

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

# show data from exhaust_FrontArrows
exhaust_FrontArrowsDisplay_2 = Show(exhaust_FrontArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_FrontArrowsDisplay_2.Representation = 'Surface'
exhaust_FrontArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_2.ColorArrayName = [None, '']
exhaust_FrontArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_FrontArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.ScaleFactor = 0.014079396799206735
exhaust_FrontArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.GlyphType = 'Arrow'
exhaust_FrontArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_FrontArrowsDisplay_2.GaussianRadius = 0.0007039698399603367
exhaust_FrontArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_FrontArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_FrontArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_FrontArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_FrontArrowsDisplay_2.ScaleTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_FrontArrowsDisplay_2.OpacityTransferFunction.Points = [-0.007355894879307142, 0.0, 0.5, 0.0, 0.11420185421706736, 1.0, 0.5, 0.0]

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

# show data from exhaust_BackArrows
exhaust_BackArrowsDisplay_2 = Show(exhaust_BackArrows, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackArrowsDisplay_2.Representation = 'Surface'
exhaust_BackArrowsDisplay_2.AmbientColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_2.ColorArrayName = [None, '']
exhaust_BackArrowsDisplay_2.DiffuseColor = [0.0, 0.0, 1.0]
exhaust_BackArrowsDisplay_2.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_2.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.ScaleFactor = 0.014254055917263031
exhaust_BackArrowsDisplay_2.SelectScaleArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.GlyphType = 'Arrow'
exhaust_BackArrowsDisplay_2.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackArrowsDisplay_2.GaussianRadius = 0.0007127027958631516
exhaust_BackArrowsDisplay_2.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_2.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackArrowsDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackArrowsDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackArrowsDisplay_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackArrowsDisplay_2.ScaleTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackArrowsDisplay_2.OpacityTransferFunction.Points = [-0.0013160721344962804, 0.0, 0.5, 0.0, 0.00953104410714719, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_3 = Show(contour1, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_3.Representation = 'Surface'
contour1Display_3.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_3.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_3.SelectOrientationVectors = 'None'
contour1Display_3.ScaleFactor = -2.0000000000000002e+298
contour1Display_3.SelectScaleArray = 'None'
contour1Display_3.GlyphType = 'Arrow'
contour1Display_3.GlyphTableIndexArray = 'None'
contour1Display_3.GaussianRadius = -1e+297
contour1Display_3.SetScaleArray = [None, '']
contour1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_3.OpacityArray = [None, '']
contour1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_3.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_3.PolarAxes = 'PolarAxesRepresentation'

# setup the color legend parameters for each legend in this view

# get color legend/bar for velocityLUT in view renderView4
velocityLUTColorBar_2 = GetScalarBar(velocityLUT, renderView4)
velocityLUTColorBar_2.Title = 'velocity'
velocityLUTColorBar_2.ComponentTitle = 'Magnitude'

# set color bar visibility
velocityLUTColorBar_2.Visibility = 0

# get color legend/bar for g_EQN_TRANSPORTLUT in view renderView4
g_EQN_TRANSPORTLUTColorBar_3 = GetScalarBar(g_EQN_TRANSPORTLUT, renderView4)
g_EQN_TRANSPORTLUTColorBar_3.Title = 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUTColorBar_3.ComponentTitle = ''

# set color bar visibility
g_EQN_TRANSPORTLUTColorBar_3.Visibility = 0

# hide data in view
Hide(intake_FrontArrows, renderView4)

# hide data in view
Hide(intake_BackArrows, renderView4)

# hide data in view
Hide(exhaust_FrontArrows, renderView4)

# hide data in view
Hide(exhaust_BackArrows, renderView4)

# hide data in view
Hide(contour1, renderView4)

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

# show data from intakeExhaust_Geometry
intakeExhaust_GeometryDisplay_3 = Show(intakeExhaust_Geometry, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
intakeExhaust_GeometryDisplay_3.Representation = 'Surface'
intakeExhaust_GeometryDisplay_3.ColorArrayName = [None, '']
intakeExhaust_GeometryDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_3.SelectOrientationVectors = 'None'
intakeExhaust_GeometryDisplay_3.ScaleFactor = 0.027035209536552432
intakeExhaust_GeometryDisplay_3.SelectScaleArray = 'None'
intakeExhaust_GeometryDisplay_3.GlyphType = 'Arrow'
intakeExhaust_GeometryDisplay_3.GlyphTableIndexArray = 'None'
intakeExhaust_GeometryDisplay_3.GaussianRadius = 0.0013517604768276215
intakeExhaust_GeometryDisplay_3.SetScaleArray = [None, '']
intakeExhaust_GeometryDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_3.OpacityArray = [None, '']
intakeExhaust_GeometryDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
intakeExhaust_GeometryDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
intakeExhaust_GeometryDisplay_3.PolarAxes = 'PolarAxesRepresentation'
intakeExhaust_GeometryDisplay_3.ScalarOpacityUnitDistance = 0.0023014537338361435
intakeExhaust_GeometryDisplay_3.ExtractedBlockIndex = 1

# show data from head
headDisplay_2 = Show(head, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
headDisplay_2.Representation = 'Surface'
headDisplay_2.AmbientColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay_2.ColorArrayName = [None, '']
headDisplay_2.DiffuseColor = [0.5019607843137255, 0.5019607843137255, 0.5019607843137255]
headDisplay_2.Opacity = 0.25
headDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
headDisplay_2.SelectOrientationVectors = 'None'
headDisplay_2.ScaleFactor = 0.008899322897195817
headDisplay_2.SelectScaleArray = 'None'
headDisplay_2.GlyphType = 'Arrow'
headDisplay_2.GlyphTableIndexArray = 'None'
headDisplay_2.GaussianRadius = 0.0004449661448597908
headDisplay_2.SetScaleArray = [None, '']
headDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
headDisplay_2.OpacityArray = [None, '']
headDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
headDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
headDisplay_2.PolarAxes = 'PolarAxesRepresentation'
headDisplay_2.ScalarOpacityUnitDistance = 0.0016640944230168922
headDisplay_2.ExtractedBlockIndex = 1

# show data from parcel
parcelDisplay_2 = Show(parcel, renderView5, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'dp_velocity'
dp_velocityPWF = GetOpacityTransferFunction('dp_velocity')
dp_velocityPWF.Points = [1.0468732896140134e-07, 0.0, 0.5, 0.0, 312.8507478755334, 1.0, 0.5, 0.0]
dp_velocityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
parcelDisplay_2.Representation = 'Surface'
parcelDisplay_2.ColorArrayName = ['POINTS', 'dp_velocity']
parcelDisplay_2.LookupTable = dp_velocityLUT
parcelDisplay_2.OSPRayScaleArray = 'dp_FROM_NOZZLE'
parcelDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay_2.SelectOrientationVectors = 'None'
parcelDisplay_2.ScaleFactor = 0.015194140002131463
parcelDisplay_2.SelectScaleArray = 'None'
parcelDisplay_2.GlyphType = 'Arrow'
parcelDisplay_2.GlyphTableIndexArray = 'None'
parcelDisplay_2.GaussianRadius = 0.0007597070001065732
parcelDisplay_2.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay_2.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay_2.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay_2.ScalarOpacityFunction = dp_velocityPWF
parcelDisplay_2.ScalarOpacityUnitDistance = 0.0055156914629405866
parcelDisplay_2.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_4 = Show(contour1, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_4.Representation = 'Surface'
contour1Display_4.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_4.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_4.Specular = 1.0
contour1Display_4.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display_4.SpecularPower = 10.0
contour1Display_4.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_4.SelectOrientationVectors = 'None'
contour1Display_4.ScaleFactor = -2.0000000000000002e+298
contour1Display_4.SelectScaleArray = 'None'
contour1Display_4.GlyphType = 'Arrow'
contour1Display_4.GlyphTableIndexArray = 'None'
contour1Display_4.GaussianRadius = -1e+297
contour1Display_4.SetScaleArray = [None, '']
contour1Display_4.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_4.OpacityArray = [None, '']
contour1Display_4.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_4.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_4.PolarAxes = 'PolarAxesRepresentation'

# show data from threshold1
threshold1Display_2 = Show(threshold1, renderView5, 'UnstructuredGridRepresentation')

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

# setup the color legend parameters for each legend in this view

# get color legend/bar for dp_TEMPLUT in view renderView5
dp_TEMPLUTColorBar_2 = GetScalarBar(dp_TEMPLUT, renderView5)
dp_TEMPLUTColorBar_2.WindowLocation = 'UpperRightCorner'
dp_TEMPLUTColorBar_2.Title = 'dp_TEMP'
dp_TEMPLUTColorBar_2.ComponentTitle = ''

# set color bar visibility
dp_TEMPLUTColorBar_2.Visibility = 0

# get color legend/bar for g_EQN_TRANSPORTLUT in view renderView5
g_EQN_TRANSPORTLUTColorBar_4 = GetScalarBar(g_EQN_TRANSPORTLUT, renderView5)
g_EQN_TRANSPORTLUTColorBar_4.Title = 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUTColorBar_4.ComponentTitle = ''

# set color bar visibility
g_EQN_TRANSPORTLUTColorBar_4.Visibility = 0

# get color legend/bar for dp_FROM_NOZZLELUT in view renderView5
dp_FROM_NOZZLELUTColorBar_2 = GetScalarBar(dp_FROM_NOZZLELUT, renderView5)
dp_FROM_NOZZLELUTColorBar_2.Position = [0.7857142857142857, 0.04269972451790634]
dp_FROM_NOZZLELUTColorBar_2.Title = 'dp_FROM_NOZZLE'
dp_FROM_NOZZLELUTColorBar_2.ComponentTitle = ''

# set color bar visibility
dp_FROM_NOZZLELUTColorBar_2.Visibility = 0

# get color legend/bar for dp_RADIUSLUT in view renderView5
dp_RADIUSLUTColorBar_2 = GetScalarBar(dp_RADIUSLUT, renderView5)
dp_RADIUSLUTColorBar_2.Title = 'dp_RADIUS'
dp_RADIUSLUTColorBar_2.ComponentTitle = ''

# set color bar visibility
dp_RADIUSLUTColorBar_2.Visibility = 0

# get color legend/bar for dp_velocityLUT in view renderView5
dp_velocityLUTColorBar_2 = GetScalarBar(dp_velocityLUT, renderView5)
dp_velocityLUTColorBar_2.Orientation = 'Horizontal'
dp_velocityLUTColorBar_2.WindowLocation = 'AnyLocation'
dp_velocityLUTColorBar_2.Position = [0.2924489795918367, 0.1502479338842975]
dp_velocityLUTColorBar_2.Title = 'dp_velocity'
dp_velocityLUTColorBar_2.ComponentTitle = 'Magnitude'
dp_velocityLUTColorBar_2.ScalarBarLength = 0.32999999999999974

# set color bar visibility
dp_velocityLUTColorBar_2.Visibility = 0

# get color legend/bar for v_magLUT in view renderView5
v_magLUTColorBar_1 = GetScalarBar(v_magLUT, renderView5)
v_magLUTColorBar_1.Title = 'v_mag'
v_magLUTColorBar_1.ComponentTitle = ''

# set color bar visibility
v_magLUTColorBar_1.Visibility = 0

# get color transfer function/color map for 'ShepardSummation'
shepardSummationLUT = GetColorTransferFunction('ShepardSummation')
shepardSummationLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.10359997302293777, 0.865003, 0.865003, 0.865003, 0.20719994604587555, 0.705882, 0.0156863, 0.14902]
shepardSummationLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for shepardSummationLUT in view renderView5
shepardSummationLUTColorBar = GetScalarBar(shepardSummationLUT, renderView5)
shepardSummationLUTColorBar.WindowLocation = 'UpperRightCorner'
shepardSummationLUTColorBar.Title = 'Shepard Summation'
shepardSummationLUTColorBar.ComponentTitle = ''

# set color bar visibility
shepardSummationLUTColorBar.Visibility = 0

# hide data in view
Hide(intakeExhaust_Geometry, renderView5)

# hide data in view
Hide(parcel, renderView5)

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

# show data from parcel
parcelDisplay_3 = Show(parcel, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
parcelDisplay_3.Representation = 'Surface'
parcelDisplay_3.ColorArrayName = ['POINTS', 'dp_velocity']
parcelDisplay_3.LookupTable = dp_velocityLUT
parcelDisplay_3.OSPRayScaleArray = 'dp_RADIUS'
parcelDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
parcelDisplay_3.SelectOrientationVectors = 'None'
parcelDisplay_3.ScaleFactor = 0.015194140002131463
parcelDisplay_3.SelectScaleArray = 'None'
parcelDisplay_3.GlyphType = 'Arrow'
parcelDisplay_3.GlyphTableIndexArray = 'None'
parcelDisplay_3.GaussianRadius = 0.0007597070001065732
parcelDisplay_3.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
parcelDisplay_3.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
parcelDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
parcelDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
parcelDisplay_3.PolarAxes = 'PolarAxesRepresentation'
parcelDisplay_3.ScalarOpacityFunction = dp_velocityPWF
parcelDisplay_3.ScalarOpacityUnitDistance = 0.0055156914629405866
parcelDisplay_3.ExtractedBlockIndex = 1

# show data from contour1
contour1Display_5 = Show(contour1, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_5.Representation = 'Surface'
contour1Display_5.ColorArrayName = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_5.LookupTable = g_EQN_TRANSPORTLUT
contour1Display_5.Specular = 1.0
contour1Display_5.SpecularColor = [1.0, 1.0, 0.4980392156862745]
contour1Display_5.SpecularPower = 10.0
contour1Display_5.OSPRayScaleArray = 'G_EQN_TRANSPORT'
contour1Display_5.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_5.SelectOrientationVectors = 'G_EQN_TRANSPORT'
contour1Display_5.ScaleFactor = 0.0025496815331280233
contour1Display_5.SelectScaleArray = 'G_EQN_TRANSPORT'
contour1Display_5.GlyphType = 'Arrow'
contour1Display_5.GlyphTableIndexArray = 'G_EQN_TRANSPORT'
contour1Display_5.GaussianRadius = 0.00012748407665640117
contour1Display_5.SetScaleArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_5.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_5.OpacityArray = ['POINTS', 'G_EQN_TRANSPORT']
contour1Display_5.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_5.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_5.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_5.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_5.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from exhaust_BackStreamTracer
exhaust_BackStreamTracerDisplay_3 = Show(exhaust_BackStreamTracer, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
exhaust_BackStreamTracerDisplay_3.Representation = 'Surface'
exhaust_BackStreamTracerDisplay_3.ColorArrayName = [None, '']
exhaust_BackStreamTracerDisplay_3.OSPRayScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_3.SelectOrientationVectors = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_3.ScaleFactor = 0.04381939768791199
exhaust_BackStreamTracerDisplay_3.SelectScaleArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_3.GlyphType = 'Arrow'
exhaust_BackStreamTracerDisplay_3.GlyphTableIndexArray = 'IntegrationTime'
exhaust_BackStreamTracerDisplay_3.GaussianRadius = 0.0021909698843955994
exhaust_BackStreamTracerDisplay_3.SetScaleArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_3.OpacityArray = ['POINTS', 'IntegrationTime']
exhaust_BackStreamTracerDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
exhaust_BackStreamTracerDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
exhaust_BackStreamTracerDisplay_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
exhaust_BackStreamTracerDisplay_3.ScaleTransferFunction.Points = [-0.04181937514679069, 0.0, 0.5, 0.0, 0.03530186375600624, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
exhaust_BackStreamTracerDisplay_3.OpacityTransferFunction.Points = [-0.04181937514679069, 0.0, 0.5, 0.0, 0.03530186375600624, 1.0, 0.5, 0.0]

# show data from threshold1
threshold1Display_3 = Show(threshold1, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display_3.Representation = 'Surface'
threshold1Display_3.AmbientColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display_3.ColorArrayName = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_3.DiffuseColor = [1.0, 0.3333333333333333, 0.0]
threshold1Display_3.LookupTable = dp_FROM_NOZZLELUT
threshold1Display_3.OSPRayScaleArray = 'dp_FROM_NOZZLE'
threshold1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display_3.SelectOrientationVectors = 'None'
threshold1Display_3.ScaleFactor = 0.008697206526994706
threshold1Display_3.SelectScaleArray = 'None'
threshold1Display_3.GlyphType = 'Arrow'
threshold1Display_3.GlyphTableIndexArray = 'None'
threshold1Display_3.GaussianRadius = 0.0004348603263497353
threshold1Display_3.SetScaleArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display_3.OpacityArray = ['POINTS', 'dp_FROM_NOZZLE']
threshold1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display_3.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display_3.PolarAxes = 'PolarAxesRepresentation'
threshold1Display_3.ScalarOpacityFunction = dp_FROM_NOZZLEPWF
threshold1Display_3.ScalarOpacityUnitDistance = 0.0050929497409951735
threshold1Display_3.ExtractedBlockIndex = 1

# setup the color legend parameters for each legend in this view

# get color legend/bar for dp_TEMPLUT in view renderView6
dp_TEMPLUTColorBar_3 = GetScalarBar(dp_TEMPLUT, renderView6)
dp_TEMPLUTColorBar_3.Position = [0.5812274368231047, 0.03305785123966942]
dp_TEMPLUTColorBar_3.Title = 'dp_TEMP'
dp_TEMPLUTColorBar_3.ComponentTitle = ''

# set color bar visibility
dp_TEMPLUTColorBar_3.Visibility = 0

# get color legend/bar for g_EQN_TRANSPORTLUT in view renderView6
g_EQN_TRANSPORTLUTColorBar_5 = GetScalarBar(g_EQN_TRANSPORTLUT, renderView6)
g_EQN_TRANSPORTLUTColorBar_5.Title = 'G_EQN_TRANSPORT'
g_EQN_TRANSPORTLUTColorBar_5.ComponentTitle = ''

# set color bar visibility
g_EQN_TRANSPORTLUTColorBar_5.Visibility = 0

# get color legend/bar for dp_FROM_NOZZLELUT in view renderView6
dp_FROM_NOZZLELUTColorBar_3 = GetScalarBar(dp_FROM_NOZZLELUT, renderView6)
dp_FROM_NOZZLELUTColorBar_3.Position = [0.8483754512635379, 0.04269972451790634]
dp_FROM_NOZZLELUTColorBar_3.Title = 'dp_FROM_NOZZLE'
dp_FROM_NOZZLELUTColorBar_3.ComponentTitle = ''

# set color bar visibility
dp_FROM_NOZZLELUTColorBar_3.Visibility = 0

# get color legend/bar for dp_NUM_DROPLUT in view renderView6
dp_NUM_DROPLUTColorBar_1 = GetScalarBar(dp_NUM_DROPLUT, renderView6)
dp_NUM_DROPLUTColorBar_1.Title = 'dp_NUM_DROP'
dp_NUM_DROPLUTColorBar_1.ComponentTitle = ''

# set color bar visibility
dp_NUM_DROPLUTColorBar_1.Visibility = 0

# get color legend/bar for dp_RADIUSLUT in view renderView6
dp_RADIUSLUTColorBar_3 = GetScalarBar(dp_RADIUSLUT, renderView6)
dp_RADIUSLUTColorBar_3.Title = 'dp_RADIUS'
dp_RADIUSLUTColorBar_3.ComponentTitle = ''

# set color bar visibility
dp_RADIUSLUTColorBar_3.Visibility = 0

# get color legend/bar for dp_velocityLUT in view renderView6
dp_velocityLUTColorBar_3 = GetScalarBar(dp_velocityLUT, renderView6)
dp_velocityLUTColorBar_3.Title = 'dp_velocity'
dp_velocityLUTColorBar_3.ComponentTitle = 'Magnitude'

# set color bar visibility
dp_velocityLUTColorBar_3.Visibility = 0

# get color legend/bar for v_magLUT in view renderView6
v_magLUTColorBar_2 = GetScalarBar(v_magLUT, renderView6)
v_magLUTColorBar_2.WindowLocation = 'UpperRightCorner'
v_magLUTColorBar_2.Title = 'v_mag'
v_magLUTColorBar_2.ComponentTitle = ''

# set color bar visibility
v_magLUTColorBar_2.Visibility = 0

# hide data in view
Hide(parcel, renderView6)

# hide data in view
Hide(exhaust_BackStreamTracer, renderView6)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'BOUND_TEMP'
bOUND_TEMPPWF = GetOpacityTransferFunction('BOUND_TEMP')
bOUND_TEMPPWF.Points = [393.0, 0.0, 0.5, 0.0, 1043.0, 1.0, 0.5, 0.0]
bOUND_TEMPPWF.ScalarRangeInitialized = 1

# get separate opacity transfer function/opacity map for 'velocity'
separate_intake_FrontStreamTracerDisplay_velocityPWF = GetOpacityTransferFunction('velocity', intake_FrontStreamTracerDisplay, separate=True)
separate_intake_FrontStreamTracerDisplay_velocityPWF.Points = [0.15321904838973519, 0.0, 0.5, 0.0, 30.080767038961703, 1.0, 0.5, 0.0]
separate_intake_FrontStreamTracerDisplay_velocityPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Crank_Angle'
crank_AnglePWF = GetOpacityTransferFunction('Crank_Angle')
crank_AnglePWF.Points = [250.04531860351562, 0.0, 0.5, 0.0, 250.07656860351562, 1.0, 0.5, 0.0]
crank_AnglePWF.ScalarRangeInitialized = 1

# get separate opacity transfer function/opacity map for 'G_EQN_TRANSPORT'
separate_contour1Display_G_EQN_TRANSPORTPWF = GetOpacityTransferFunction('G_EQN_TRANSPORT', contour1Display, separate=True)
separate_contour1Display_G_EQN_TRANSPORTPWF.Points = [-0.019999999552965164, 0.0, 0.5, 0.0, 0.019999999552965164, 1.0, 0.5, 0.0]
separate_contour1Display_G_EQN_TRANSPORTPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'v_mag'
v_magPWF = GetOpacityTransferFunction('v_mag')
v_magPWF.Points = [4.708444910864552e-07, 0.0, 0.5, 0.0, 35.56390301347899, 1.0, 0.5, 0.0]
v_magPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'dp_NUM_DROP'
dp_NUM_DROPPWF = GetOpacityTransferFunction('dp_NUM_DROP')
dp_NUM_DROPPWF.Points = [0.0036555055994540453, 0.0, 0.5, 0.0, 3846465.5, 1.0, 0.5, 0.0]
dp_NUM_DROPPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'Normals'
normalsPWF = GetOpacityTransferFunction('Normals')
normalsPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0000001057108072, 1.0, 0.5, 0.0]
normalsPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'dp_TEMP'
dp_TEMPPWF_1 = GetOpacityTransferFunction('dp_TEMP')
dp_TEMPPWF_1.Points = [306.0483093261719, 0.0, 0.5, 0.0, 306.0483093261719, 0.0, 0.5, 0.0, 529.181396484375, 1.0, 0.5, 0.0]
dp_TEMPPWF_1.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'ShepardSummation'
shepardSummationPWF = GetOpacityTransferFunction('ShepardSummation')
shepardSummationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.20719994604587555, 1.0, 0.5, 0.0]
shepardSummationPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'dp_RADIUS'
dp_RADIUSPWF = GetOpacityTransferFunction('dp_RADIUS')
dp_RADIUSPWF.Points = [1.312970425715321e-07, 0.0, 0.5, 0.0, 0.0002429911692161113, 1.0, 0.5, 0.0]
dp_RADIUSPWF.ScalarRangeInitialized = 1

# get separate opacity transfer function/opacity map for 'velocity'
separate_intake_FrontArrowsDisplay_velocityPWF = GetOpacityTransferFunction('velocity', intake_FrontArrowsDisplay, separate=True)
separate_intake_FrontArrowsDisplay_velocityPWF.Points = [8.223022689899208, 0.0, 0.5, 0.0, 102.11594362171299, 1.0, 0.5, 0.0]
separate_intake_FrontArrowsDisplay_velocityPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(intake_FrontStreamTracer)
# ----------------------------------------------------------------